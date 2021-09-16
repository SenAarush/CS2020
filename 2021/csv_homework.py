import csv
def read():
    rows=[]
    with open('file.csv','r') as csvfile:
        csvreader=csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
        for row in rows:
            print(row)
def createfile():
    with open("file.csv",'w') as csvfile:
        n=int(input("Enter no. of records: "))
        for i in range(0,n):
            records=[]
            cus_id=input("Enter your id: ")
            dest=input("Enter your destination: ")
            days=int(input("Enter days: ")) 
            fare=int(input("Enter fare: "))
            record=[cus_id,dest,days,fare]
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow(record)
def checkdest():
    f=input('Enter filename with extension: ')
    rows=[]
    with open(f,'r') as csvfile:
        csvreader=csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
        for row in rows:
            if int(row[2])<15:
                print(row)
def createtabfile():
    with open('file.csv','w') as csvfile:
        csvwriter=csv.writer(csvfile,delimiter='\t')
        n=int(input("Enter no. of records: "))
        for i in range(0,n):
            records=[]
            cus_id=input("Enter your id: ")
            dest=input("Enter your destination: ")
            days=int(input("Enter days: ")) 
            fare=int(input("Enter fare: "))
            record=[cus_id,dest,days,fare]
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow(record)
'''createtabfile()'''              
'''checkdest()'''
read()
 
