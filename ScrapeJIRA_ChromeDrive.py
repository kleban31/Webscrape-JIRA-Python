from bs4 import BeautifulSoup as bs
import requests as rq
from requests_html import HTMLSession
from lxml import html
import re
import json
from selenium import webdriver
from datetime import datetime

with open("Variables.xml", "r") as x:
    vxml = bs(x,'lxml')

vxml=bs('Variables.xml')

url = vxml.find('LoginURL').string
surl=vxml.find('SearchURL').string
uname=vxml.find('user').string
pword=vxml.find('password').string


driver = webdriver.Chrome()

driver.get(url)
def login():
    driver.find_element_by_id("login-form-username").send_keys(uname)
    driver.find_element_by_id("login-form-password").send_keys(pword)
    driver.find_element_by_id("login-form-submit").click()
login()

driver.get(surl)
html = driver.page_source
content = bs(html, features='lxml')





def hasDik(tag):
    return tag.has_attr('data-issuekey')

IssueTables = content.findAll('table',attrs={'id':'issuetable'})

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
        td_rep =  DIK.find('td',attrs={'class':'reporter'})
        td_created =  DIK.find('td',attrs={'class':'created'})
        td_updated = DIK.find('td',attrs={'class':'updated'})
        s=td_status.find('span')
        s = s.text
        s = s.strip()
        sum=td_summary.find('p')
        sum = sum.text
        sum = sum.strip()
        rep=td_rep.text
        rep = rep.strip()
        if NewURLisFile=="true":
            created=td_created.text
            updated=td_updated.text
        else:
            created=td_created.span['title']
            updated=td_updated.span['title']
        # print(ik + ' - ' + s.text + ' - ' + sum.text)
        dic = {'Key':ik, 'Status':s, 'Summary':sum,'Reporter':rep,'IssueCreatedDate':created,'UpdatedDate':updated, 'RefreshDate':now_}
        arr.append(dic)




j = json.dumps(arr,indent=4)
with open('MainScripts/JIRAData.json','w') as NewJ:
    NewJ.write(j)

with open('MainScripts/JIRAData.json','r') as NewJ:
    rj = NewJ.read()

print(rj)

if UseDriver=="true":
    driver.close()
