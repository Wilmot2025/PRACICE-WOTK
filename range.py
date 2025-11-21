# range of i (1,4) --1,2,3
# first step  i=1, j=(1,2)  --- * ---next line
# second step i=2  j=(1,3)  --- **---- next line
# third step  i=3  j=(1,4)  --- ***--- next line
for i in range(1,4):
    for j in range(1,i+1):
        print("*",end=" ")
        print() 

for i in range(1,4):
    for j in range(2,i+1):
        print(j,end=" ")
        print() 

    for i in range(1,4):
        for j in range(3,i+1):
            print(i,end=" ")
            print()

    for i in range(1,4):
        for j in range(4,i+1):
            print(i,end=" ")
            print()

for i in range(0, 2):    ##  2 times 
    print("this is my first for loop")
    for j in range(0,1):   ## 1 time 
        print("the value of i: ", i, "the value of j:", j)

for i in range(0, 3):    ##  2 times 
    print("this is my second for loop")
    for T in range(0,2):   ## 1 time 
        print("the value of i: ", i, "the value of T:", T)

for i in range(0, 4):    ##  2 times    
    print("this is my third for loop")  
    for O in range(0,3):   ## 1 time 
        print("the value of i: ", i, "the value of O:", O)

 
 
    