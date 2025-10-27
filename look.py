
for i in range(1,11):
    print(i)
    print("Wilmot")
    print("Okai")
    print("wilmot okai jr")

# Second loop to print Sharik 5 times
for i in range(5):
    print("Sharik")

# Loop steps explanation:
# step 1: i starts at 0 (initialization)
# step 2: check if i < 5 (condition)
# step 3: print "Sharik" (task)
# step 4: i increases by 1 (increment)

for i in range(5):
    print("Sharik")
print("Wilmot Okai Jr")
for i in range(2, 21, 2):
    print(i)    
for i in range(1, 21, 2):
    print(i)    

Fruit= ( "banana", "mango", "orange", "pineapple", "apple")
for i in Fruit:
    print(i)    

# creating list of squares of first 10 whole number
sq=[]  
print(f"before entering the loop {sq}")
for i in range (10):
    square = i**2
    sq.append(square)
print(sq)   

# create a list of double numbers from 1 to 10
double=[]
for i in range (1,11):  
    double.append(i*2)  
print(double)   

# List of comprehension, a short way of creating list.
sqr=[i**2 for i in range(10)]       # take the value from 0 to 9 and suqareit
sqr2=[i**2 for i in range(1,11,2)]  
print(sqr)

sq_even = [i**2 for i in range(10) if i%2==0]   #squaring only even numbers
print(sq_even)