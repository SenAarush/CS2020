#write a python program that fetches reuslts from event table of pet database where type is 'kennel'

import mysql.connector as m
#not checking if its connected
obj=m.connect(host='localhost',user='root',passwd='5546',database='pet')

dbcursor=obj.cursor()
dbcursor.execute("select * from event where type="kennel")
data=dbcursor.fetchall()
print(data)
obj.close()
