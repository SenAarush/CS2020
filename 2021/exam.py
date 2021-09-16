def EXTRA_ELE(A,B):
    for i in A:
        if i not in B:
            print(i)
   
    
B=[23,8,19,4,14,11,5]
A=[14,21,5,19,8,4,23,11]
EXTRA_ELE(A,B)
