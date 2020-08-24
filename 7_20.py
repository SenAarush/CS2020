#WAP to display the output ½ + 2/3 + ¾ + 4/5 +….
'''a = int(input("Enter the range"))
n=0
s=0
for i in range(1,a+1):
    n=i+1
    s=s+(i/n)
print(s)'''

#WAP to display the output 1+x2+x3+x4+…
'''a = int(input("Enter the range: "))
x= int(input("Enter a number: "))
s=0
for i in range(0,a+1):
    s=s+(x**i)
print(s)'''

#WAP to display the output 0, 3, 8, 15, 24, 35, ……
'''a=int(input("Enter the range: "))#10 
s=0
print(0)
for i in range(3, a+1,2):#3,5,7,9
    s=s+i#3,8,15,24
    print(s)'''##0 is not being printed

#WAP to display the output 2/9-5/13+8/17+……

#WAP to display the output 1+(1+2)+(1+2+3)+(1+2+3+4)+……
'''a=int(input("Enter the range: "))
fs=0
sum=0
for k in range(1,a+1):
    fs=0
    for i in range(1,k+1):
        fs+=i
    sum+=fs
print(sum)'''
