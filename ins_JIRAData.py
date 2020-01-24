import sqlite3 as sql
import json
import os
from datetime import datetime

db = sql.connect('MainScripts/JIRATable.sqlite')
c = db.cursor()
#
# c.execute('drop table if exists JIRAData')

c.execute('''create table if not exists JIRAData (Key text, Status text, Summary text,Reporter text,IssueCreatedOn text, IssueUpdatedOn text, RefreshDate text)''' )
#
ins = 'insert into JIRAData (Key,Status,Summary,Reporter,IssueCreatedOn,IssueUpdatedOn,RefreshDate) values (?,?,?,?,?,?,?)'
#
#
with open('MainScripts/JIRAData.json','r') as f:
    JData = json.load(f)
#
i = 0
#


for r in JData:
    RefreshDate = JData[i]['RefreshDate']
    val=(JData[i]['Key'],JData[i]['Status'],JData[i]['Summary'],JData[i]['Reporter'],JData[i]['IssueCreatedDate'],JData[i]['UpdatedDate'],RefreshDate)
    i = i+1
    c.execute(ins,val)
    print(c.fetchall())

db.commit()

# c.execute('select count(*) From JIRAData')
# res = c.fetchall()

# for row in res:
#     print(row)


# db.close()

# os.remove('JIRATable.sqlite')




# print(JData[0]['Key'])
# print(JData[1]['Key'])
