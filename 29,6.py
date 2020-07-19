#To find out if two angles are complementary or supplementary

'''a=int(input("Enter the measure of 1st angle"))
b=int(input("Enter the measure of 2nd angle"))
c=a+b
if c==90:
     print(a, b, "Are complementary angles")
elif c==180:
     print(a, b, "Are supplementary angles")
else:
     print(a, b, "Are neither supplementary or complementary angles")'''
     
#To display a menu and take action from user input

'''a = print("Enter C to calculate values in celcius or F to display values in farenheit")
if a==C:
     b=int(input("Enter the value in farenheit"))
     ans=(b-32)/1.8
     print("The value in celcius is ", ans)
elif a==F:
     b=int(input("Enter the value in celcius"))
     ans=(b-32)/1.8
     print("The value in farenheit is ", ans)
else:
     print("Error!....choose correct option to compute answer"  '''

#Ask the user which figure's volume he/she wants to calculate

'''a = print("Which figure's volume do you want to compute? A=sphere, B=cuboid C=cube")

if a==A:
     b=int(input("Enter value of r"))
     ans=float((4*3.14*b*b*b)/3)
     print(ans, "is the volume of the sphere")
elif a==B:
     l=int(input("Enter value of l"))
     b=int(input("Enter value of b"))
     h=int(input("Enter value of h"))
     k=float(l*b*h)
     print(k, "is the volume of the cuboid")
elif a==C:
     l=int(input("Enter value of l"))
     b=int(input("Enter value of b"))
     ans=float(l*b)
     print(ans, "is the volume of the cube")
else:
     print("Error!......Wrong option entered")'''

#Calculate stream, from entered marks

'''s=int(input("Enter the marks of Science out of 100"))
e=int(input("Enter value of english out of 100"))
m=int(input("Enter value of maths out of 100"))

if s>=80 and e>=80 and m>=80:
     print("You are mopst eligible for the Pure Science stream!")
elif s==80 and e>=80 and m>=60:
     print("Congratulations, you are most eligible for the Bio-Science stream!")
elif s==60 and e>=60 and  m>=60:
     print("Congratulations, you are mopst eligible for the Commerce stream!")
else:
     print("Congratulations, you are most eligible for the libral arts! steam")'''








































#Calculate stream, from entered marks

s=int(input("Enter the marks of Science out of 100"))
e=int(input("Enter value of english out of 100"))
m=int(input("Enter value of maths out of 100"))

if s>=80 and e>=80 and m>=80:
     print("You are mopst eligible for the Pure Science stream!")
elif s==80 and e>=80 and m>=60:
     print("Congratulations, you are most eligible for the Bio-Science stream!")
elif s==60 and e>=60 and  m>=60:
     print("Congratulations, you are mopst eligible for the Commerce stream!")
else:
     print("Congratulations, you are most eligible for the libral arts!")



