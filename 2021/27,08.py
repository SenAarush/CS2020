#A text file named MESSAGE.TXT contains some text. Another text file named SMS.TXT needs to be created such that it would store only the first 150 characters from the file MESSAGE.TXT Write a user-defined function LongToShort() in Python that would perform the above task of creating SMS.TXT from the already existing file MESSAGE.TXT
'''
def LongToShort():
    f=open('MESSAGE.txt','r')
    p=open('SMS.txt','w+')
    for i in f.read(150):
            p.write(i)
    p.close()
    f.close()
LongToShort()
'''
#2. Write a Python program to write a Python list of lists to a csv file. After writing the CSV file, read the CSV file and display the country wise count. The file should contain country code and country name

import csv
'''with open("f.csv", 'w+',newline='') as k:
    df=[['India','700068'],['India','700168'],['Argentina','710068'],['South Africa','500068']]
    writer_object=csv.writer(k)
    writer_object.writerows(df)
    k.close()'''
with open("f.csv", 'r') as k:
    l=[]
    for i in k:
        l.append(i)
    print(l)
        
    
    



