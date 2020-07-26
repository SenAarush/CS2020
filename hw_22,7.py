#9+99+8+89+7+…n terms
'''a=int(input("Enter the range: "))
s=0
n=0
for i in range(1,a+1):
    n=10-i
    n=str(n)
    l=str(n+"9")
    l=int(l)
    print(l)
    n=int(n)
    s=s+n+l
    print(s)
print(s)'''

#(1*2)+(2*3)+(3*4)+….+(19*20)
'''s=0
imt=0
for i in range(1,21):
    imt=0
    imt=i*(i+1)
    s=s+imt
    print(s)
print(s)'''

#1+¾ 5/9+ … n terms
'''n=int(input("Enter the range: "))
a=-1
s=0
k=0
for i in range(1,n+1):#-1,1
    a=a+2#1,3
    k=(a)/(i**2)
    s=s+k
print(s)'''

#1+a/2!+a/3!+ ….+a/n!
'''a=int(input("Enter a number"))
for i in range(1,a+1):'''

#1-a/2+3-a/4+5-a/6+….. n terms
'''n=int(input("Enter the range: "))
a=int(input("Enter the value of a: "))
s=0
for i in range(1,n+1):
    if i%2==0:
        s=s-(a/i)
    else:
        s=s+i
print(s)'''

#a-a^3/5+a^5/9–a^7/13………… n terms
'''n=int(input("Enter the range: "))
a=int(input("Enter the value of a: "))
s=0
d=-3
e=-1
for i in range(1,n+1):
    d=d+4
    e=e+2
    if i%2==0:
        print(s,a,e,d)
        s=s-(a**e/d)
        print(s)
    else:
        print(s,a,e,d)
        s=s+(a**e/d)
        print(s)'''
    

