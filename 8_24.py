#Check if the number entered is special
'''a=int(input("Enter a number: "))
b=a
fact=1
s=0
while a!=0:
    d=a%10#5;4;1
    print(a,d)
    for i in range(1,d+1):
        fact*=i
    s+=fact#120;144;145
    fact=1
    a=a//10
if s==b:
    print("The given number, ", b,"is a special number")
else:
    print("The given number, ", b,"is not a special number")'''

#Check if the number entered is niven
'''a=int(input("Enter a number: "))
b=a
s=0
while a!=0:
    d=a%10
    s+=d
    a=a//10
if b%s==0:
    print("The given number", b, "is a Niven number")
else:
    print("The given number", b, "is not a Niven number")'''

#Check if the number entered is Armstrong number
'''a=int(input("Enter a number: "))
b=a
k=a
ctr=0
s=0
while a!=0:
    d=a%10
    ctr+=1
    a=a//10
while b!=0:
    c=b%10
    s+=c**ctr
    b=b//10
if s==k:
    print("The given number", k,"is an Armstrong number")
else:
    print("The given number", k,"is not an Armstrong number")'''

#Display the max and the min of a multiple digit number
'''a=int(input("Enter a number: "))
k=0
l=0
while a!=0:
    d=a%10
    a=a//10
    if d>k:
        k=d
    else:
        l=d
print(k)
print(d)'''




