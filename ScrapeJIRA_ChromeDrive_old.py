from bs4 import BeautifulSoup as bs
import requests as rq
from requests_html import HTMLSession
from lxml import html
import re
import json
from selenium import webdriver
from datetime import datetime


url = 'https://jira.amchealth.com/login.jsp'
NewURL = 'https://jira.amchealth.com/secure/Dashboard.jspa'

driver = webdriver.Chrome()

driver.get(url)
def login():
    driver.find_element_by_id("login-form-username").send_keys('mkleban')
    driver.find_element_by_id("login-form-password").send_keys('AMCamc420$')
    driver.find_element_by_id("login-form-submit").click()
login()

driver.get(NewURL)
html = driver.page_source

content = bs(html, features='lxml')


def hasDik(tag):
    return tag.has_attr('data-issuekey')

IssueTables = content.findAll('table',attrs={'class':'issue-table'})

print('Num of IssueTables: ' + str(len(IssueTables)))

arr = []
dic = {}



now = datetime.now()
now_ = now.strftime("%m/%d/%y %H:%M:%S")

for it in IssueTables:
    tr_DIKs = it.findAll(hasDik)
    for DIK in tr_DIKs:
        ik = DIK['data-issuekey']
        td_status = DIK.find('td',attrs={'class':'status'})
        td_summary = DIK.find('td',attrs={'class':'summary'})
        s=td_status.find('span')
        sum=td_summary.find('p')
        # print(ik + ' - ' + s.text + ' - ' + sum.text)
        dic = {'Key':ik, 'Status':s.text, 'Summary':sum.text, 'CreatedOn':now_}
        arr.append(dic)




j = json.dumps(arr,indent=4)
with open('MainScripts/JIRAData.json','w') as NewJ:
    NewJ.write(j)

with open('MainScripts/JIRAData.json','r') as NewJ:
    rj = NewJ.read()

print(rj)

driver.close()
