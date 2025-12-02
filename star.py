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
    
n = 5
for i in range(n):
    for i in range(n+i):
        print(" ",end="")
    for j in range(n+1):
        print("*",end="")
    print()

    n = 5
for i in range(n):
    for i in range(n-i):
        print(" ",end="")
    for j in range(n-2):
        print("*",end="")
    print()

for i in range(1, 5):
                    for j in range(1,5):
                        if (j <= 5 - i):
                           print("*", end = "")
                        else:
                           print(" ", end= "")
                    print()


for i in range(1, 7):
                    for j in range(1,7):
                        if (j <= 5 - i):
                           print("*", end = "")
                        else:
                           print(" ", end= "")
                    print()
