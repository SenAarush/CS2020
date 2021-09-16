'''A binary file “student.dat” has structure [admission_number, Name,
percentage]. Write a function countrec( ) in python that would read
contents of file “students.dat” and display the details of those students
whose percentage is above 75. Also display number of students scoring
above 75%.'''
import pickle
def countrec():
    f=open('student.dat','rb')
    l=pickle.load(f)
    count=0
    for row in l:
        if int(row[2])>75:
            print(row[1],"'s score is above 75%")
            print("admission no.:", row[0])
            print("%",row[2])
            count+=1
    print("Total no. of students with score above 75% is:",count)
    f.close()
def CreateFile():
    f=open('student.dat','wb')
    n=int(input("Enter total no. of records to enter: "))
    main=[]
    for row in range(0,n):
        record=[]
        adno=int(input("Enter student admission no.: "))
        adnam=input("Enter student name: ")
        adper=int(input("Enter percentage: "))
        record=[adno,adnam,adper]
        main.append(record)
    pickle.dump(main,f)
    f.close()
def read():
    f=open('student.dat','rb')
    l=pickle.load(f)
    for row in l:
        print(row)
    f.close()
countrec()

        
    



