
'''a=int(input("Enter the range: "))
fs=0
b=1
for i in range(0,a+1): 
    fs+1=b  
    b=sum      
    print(fs)'''
#Write a program to check if the numbers inputted by the user are twin primes
'''a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
ctr=1
if a>b:
    for i in range(1,a):
        if a%i==0 and b%i==0:
            ctr+=1
    if ctr==2 and a-b==2:
        print("The given numbers are twin primes")
    else:
        print("The given numbers are not twin primes")
elif b>a:
    for i in range(1,a):
        if a%i==0 and b%i==0:
            ctr+=1
    if ctr==2 and b-a==2:
        print("The given numbers are twin primes")
    else:
        print("The given numbers are not twin primes")'''

'''#WAP to display the series 1+3+5+7+……
a=int(input("Enter the range: "))
no=0
for i in range(1,a+1,2):
    no+=i
print(no)'''

#WAP to display the series 2-4+6-8+8-2+……
''''a=int(input("Enter the number of terms to diplay: "))
t=2
s=0
for i in range(1,a+1,):
    if i%2==0:
        s=s-t
    else:
        s=s+t
    t=t+2
print(s)'''


#WAP to display the series 1!+2!+3!+4!
'''a=int(input("Enter the range: "))
fact=1
sum=0
for k in range(1,a+1):
    fact=1
    for i in range(1,k+1):
        fact*=i
    sum+=fact
print(sum)'''
