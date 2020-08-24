#WAP TO ACCEPT A NUMBER FROM THE USER AND DISPLAY THE DIGITS SEPERATELY
'''num=int(input("Enter a number: "))
while num!=0:
    d=num%10
    print(d)
    num=num//10'''
"""#WAP TO ACCEPT A NUMBER FROM THE USER AND DISPLAY THE SUM OF THE DIGITS
num=int(input("enter a number"))
s=0
while num!=0:
    d=num%10
    s+=d
    num=num//10
print(s)"""
#WAP TO ACCEPT A NUMBER A DIPLAY ONLY THE EVEN DIGITS
'''a= int(input("Enter a number: "))
d=0
while a!=0:
    d=a%10
    if d%2==0:
        print(d)
    a=a//10'''


"""#WAP TO ACCEPT ANUMBER FROM THE USER WETHER IT IS A DUCK NUMBER OR NOT
num=int(input('enter a number'))
c=0
while num!=0:
    d=num%10
    if d==0:
        c+=1
    num=num//10
if c>=1:
    print("it is  a duck number")
else:
    print("it is not a duck number")"""
"""#WAP TO ACCEPT A NUMBER AND DIPLAY IT'S INVERSE
num=int(input('enter a number'))
while num!=0:
    d=num%10
    print(d,end="")
    num//=1"""