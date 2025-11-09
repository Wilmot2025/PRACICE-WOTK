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



        

 
 
    