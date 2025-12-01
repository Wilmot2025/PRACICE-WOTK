# how to used star in python

print("**********")
print("*        *") 

n=5
for i in range(n):
    for i in range(n):
        print(" ",end="")
    for i in range(n-i):  
        print("*",end="")
    print() 
    