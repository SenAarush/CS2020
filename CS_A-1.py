##Kindly Uncomment out each program to see its output.
##Questions are written on top of each program



#WAP that reads three integers and displays them in ascending order.
'''a=int(input("Enter an integer "))
b=int(input("Enter an integer "))
c=int(input("Enter an integer "))

if  a<b<c:
    print(a, "<" ,b, "<", c)
elif  a<c<b:
    print(a, "<" ,c, "<", b)
elif b<c<a:
    print(b, "<" ,c, "<", a)
elif b<a<c:
    print(b, "<" ,a, "<", c)
elif  c<a<b:
    print(c, "<" ,a, "<", b)
elif c<b<a:
    print(c, "<" ,b, "<", a)'''

#WAP to accept a year and check whether it is a leap year or not. (A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400.)
'''a=int(input("Enter a year "))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print(a, "is a leap year!")
        else:
            print(a, 'is not a leap year')
    else:
        print(a, 'is not a leap year')
else:
    print(a, 'is not a leap year')'''

#WAP to accept a three digit number and display its reverse.
'''a=str(input("Enter a 3 digit integer "))
b=a[2]+a[1]+a[0]
print(b)'''

#WAP to accept a date (DDMMYYYY) and display as follows : ;Input : 22102020; Output : 22 October 2020
'''a=str(input("Enter a date DDMMYYYY "))  
day = a[0]+a[1]
year = a[4]+a[5]+a[6]+a[7]
month = int(a[2]+a[3])
if month==1:
    print("The date is ", day, "January", year)
elif month==2:
    print("The date is ", day, "February", year)
elif month==3:
    print("The date is ", day, "March", year)
elif month==4:
    print("The date is ", day, "April", year)
elif month==5:
    print("The date is ", day, "May", year)   
elif month==6:
    print("The date is ", day, "June", year)
elif month==7:
    print("The date is ", day, "July", year)
elif month==8:
    print("The date is ", day, "August", year)
elif month==9:
    print("The date is ", day, "September", year)
elif month==10:
    print("The date is ", day, "October", year)
elif month==11:
    print("The date is ", day, "November", year)
else:
    print("The date is ", day, "December", year)'''

#Write a menu driven program based on the given criteria, to input name, address, amount of purchase and type of purchase (Laptop or Desktop). Compute and display the net amount to be paid by acustomer with his name and address.

'''c_name = input("Enter the name of Customer: ")
c_address = input("Enter customer address: ")
a = float(input("Enter amount of purchase: "))
ty = int(input("Type of Purchase\n enter 1 for LAPTOP \n enter 2 for PC: "))
tn = float(0)
if ty==1:
    if a<=25000:
        tn=a-((0/100)*a)
    elif a>25000 and a<=57000:
        tn=a-((5/100)*a)
    elif a>57000 and a<=100000:
        tn=a-((75/1000)*a)
    elif a>100000:
        tn=a-((10/100)*a)
    ty=str("LAPTOP")
    print("\n\n\n\nThank you for choosing our store!\n Name:",c_name,"\n Address: ", c_address, "\n Amount of Purchase: ", a, "\n Product Type: ", ty,"\n Amount payable: ", tn)
elif ty==2:
    if a<=25000:
        tn=a-((5/100)*a)
    elif a>25000 and a<=57000:
        tn=a-((75/1000)*a)
    elif a>57000 and a<=100000:
        tn=a-((10/100)*a)
    elif a>100000:
        tn=a-((15/100)*a)
    ty=str("PC")
    print("\n\n\n\nThank you for choosing our store!\n Name:",c_name,"\n Address: ", c_address, "\n Amount of Purchase: ", a, "\n Product Type: ", ty,"\n Amount payable: ", tn)
else:
    print("\n\n\nSorry, product not found. Kindly choose from the given menu")'''