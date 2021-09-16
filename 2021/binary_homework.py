import pickle
def CreateFile():
    f=open('book.dat','wb')
    n=int(input("Enter the no. of records: "))
    main=[]
    for i in range(0,n):
        record=[]
        bno=int(input("Enter book no.: "))
        bname=input("Enter book name: ")
        bauthor=input("Enter Book author: ")
        bprice=int(input("Enter the price: "))
        record=[bno,bname,bauthor,bprice]
        main.append(record)
    pickle.dump(main,f)
    f.close()
def read():
    f=open('book.dat','rb')
    l=pickle.load(f)
    print(l)
    f.close()
def counting(price):
    f=open('book.dat','rb')
    l=pickle.load(f)
    count=0
    for row in l:
        if int(row[3])>price:
            print(row[1])
            count+=1
    print(count)
    f.close()
def Update_book():
    f=open('book.dat','rb+')
    l=pickle.load(f)
    main=[]
    for row in l:
        j=int(input('Enter new price: '))
        row[3]=j
        main.append(row)
    f=open('book.dat','wb')
    pickle.dump(main,f)
def Filter_book(author):
    import os
    f=open('book.dat','rb')
    j=open('book_new.dat','wb')
    l=pickle.load(f)
    for i in l:
        if i[2]==author:
            pickle.dump(i,j)
    j.close()
    f.close()
    os.remove('book.dat')
'''CreateFile()'''
'''counting(1)'''
'''Update_book()'''
'''a=input("Enter name of author: ")
Filter_book(a)'''
read()


    
            
