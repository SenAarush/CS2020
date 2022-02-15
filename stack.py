#WAP to add an employee name to a list using PUSH (employee) and display the list. Both the functions should implement LIFO.
'''s=[]
top = None

def top(stk):
    if len(stk)==0:
        print("Underflow!")
    else:
        top = len(stk) - 1
        return top
def push(item, stk):
    stk.append(item)
    top(stk)

def peek(stk):
    if len(stk)==0:
        print("underflow")
    else:
        t = top(stk)
        print(stk[t],"<--top")
        for i in range(t-1,-1, -1):
            print(stk[i])
def pop(stk):
    if len(stk)==0:
        print("underflow")
    else:
        t = top(stk)
        return stk.pop(t)

while True:
    ch = int(input("What would you like to do?\n1. Push\n2. Peek\n3. Pop\nEnter option: "))
    if ch==1:
        item = (input("Enter employee to add to stack: "))
        push(item,s)
        print("Press any key to continue...")
    elif ch==2:
        peek(s)
        print("Press any key to continue...")
    elif ch==3:
        print(pop(s))
        print("Press any key to continue...")
    else:
        print("Wrong Input!!")
        print("Press any key to continue...")'''
## WAMBP to add, peek, delete and display the record of LIBRARY using list as stack data structure in python. Record of LIBRARY contains the information Book ID, Book type and Book cost.

'''LIBRARY = []
top = None

def top(stk):
    if len(stk)==0:
        print("Underflow!")
    else:
        top = len(stk) - 1
        return top
def push(item, stk):
    stk.append(item)
    top(stk)

def peek(stk):
    if len(stk)==0:
        print("underflow")
    else:
        t = top(stk)
        print(stk[t],"<--top")
        for i in range(t-1,-1, -1):
            print(stk[i])
def pop(stk):
    if len(stk)==0:
        print("underflow")
    else:
        t = top(stk)
        return stk.pop(t)

while True:
    ch = int(input("What would you like to do?\n1. Push\n2. Peek\n3. Pop\nEnter option: "))
    if ch==1:
        item = (input("Enter record to add to stack [BookID, Book_type, Book_cost]: "))
        push(item,LIBRARY)
        print("Press any key to continue...")
    elif ch==2:
        peek(LIBRARY)
        print("Press any key to continue...")
    elif ch==3:
        print(pop(LIBRARY))
        print("Press any key to continue...")
    else:
        print("Wrong Input!!")
        print("Press any key to continue...")'''

#Create a dictionary containing names and marks as key value pairs of 6 students. Write a program, with separate user defined functions to perform the following operations: a. Push the keys (name of the student) of the dictionary into a stack, where the corresponding value (marks) is greater than 75. b. Pop c. Display the content of the stack


dict={90: 'aarush', 60: 'srinjoy', 89: 'aarya'}
LIBRARY = []
top = None
##Creates dictionary
'''while i!=6:
    global dict
    name = input("Enter name:: ")
    marks = int(input("Enter marks:: "))
    dict[name] = marks
    i+=1'''
l1=dict.items()
def top(stk):
    if len(stk)==0:
        print("Underflow!")
    else:
        top = len(stk) - 1
        return top
def push(item, stk):
    stk.append(item)
    top(stk)

def peek(stk):
    if len(stk)==0:
        print("underflow")
    else:
        t = top(stk)
        print(stk[t],"<--top")
        for i in range(t-1,-1, -1):
            print(stk[i])
def pop(stk):
    if len(stk)==0:
        print("underflow")
    else:
        t = top(stk)
        return stk.pop(t)
def over75():
    for i in l1:
        if i[0]>75:
            push(i[1],LIBRARY)
        else:
            print(i[1], "doesn't fulfill requirements")
while True:
    ch = int(input("What would you like to do?\n1. Push\n2. Peek\n3. Pop\nEnter option: "))
    if ch==1:
        over75()
        print("Press any key to continue...")
    elif ch==2:
        peek(LIBRARY)
        print("Press any key to continue...")
    elif ch==3:
        print(pop(LIBRARY))
        print("Press any key to continue...")
    else:
        print("Wrong Input!!")
        print("Press any key to continue...")


