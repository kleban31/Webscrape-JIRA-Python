import json
import sqlite3 as sql


db = sql.connect('MainScripts/JIRATable.sqlite')
c = db.cursor()

def ce(cmd):
    c.execute(cmd)

sel = 'select * from jiradata'

ce(sel)

FD = c.fetchall()


arr=[]
dic={}


for row in FD:
    dic = {'Key':row[0],'Status':row[1],'Summary':row[2].strip(),'Reporter':row[3].strip(),'IssueCreatedOn':row[4],'IssueUpdatedOn':row[5],'RefreshDate':row[6]}
    arr.append(dic)

j = json.dumps(arr,indent=4)

with open('MainScripts/FullJiraData.json','w') as NewJ:
    NewJ.write(j)
