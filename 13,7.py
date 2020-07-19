#WAP to display all the factors of a number

'''a = int(input("Enter a number: "))
i=1
while a%i==0:
    print(i)
    i+=1'''


#WAP to display the even factors of a number

'''a=int(input("Enter a number: "))
ctr=0
for i in range(1,a+1):
    if a%i==0 and i%2==0:
        print(i)
        ctr+=1

if ctr==0:
    print(a, "has no even factors")'''
    
#WAP to check whether a number is a perfect number or not (sum of factors except the number  itself should be equal to the number. Eg: 6=1+2+3)

'''a = int(input("Enter a number: "))
chk=0
for i in range(1,a):
    if a%i==0:
        chk=chk+i
if chk==a:
    print(a, "is a perfect number")
else:
    print(a, "is not a perfect number")'''

#WAP to check for prime numbers
a=int(input("Enter a number: "))
ctr=0
for i in range(1,a+1):
    if a%i==0:
        ctr+=1
if ctr==2:
    print(a, "is a prime number")
else:
    print(a, "is not a prime number")
              