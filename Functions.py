def greet(Wilmot):
    print(f"Good Morning,{Wilmot}!")    
greet("wilmot")
greet("Saybioh") 
greet(" Ritchie")  
greet("Chreish")
greet("George")
# Function => 
# what is function in python =>

def my_function():
    print("This is Wilmot")
    print("this is Saybioh")
    print("this is Cherish")

print("This is the first time i am calling my function")
my_function()  # function call

print("This is the second time i am calling my function")
my_function()   

a = 5
b = 10
print("The sum of a and b is : ", a + b)
print("it's the second time i am calling my function")
my_function()  # function call


for i in range(3): 
    print("it's the third time i am calling my function")
    my_function()   
print("i")
print("it's the third time i am calling my function")
my_function() 


# function => it's the block of code. 
# => and we can use it whenever we want.
# => we can save our time and effort.

# how to define a function in python =>
# function definition syntax :-
def Wilmot_function():
    print("This is Togar")


Wilmot_function()  # function call

# 1. def => it is keyword to define a function.
# 2. Wilmot_function => it is the name of function.
# 3. () => parentheses are used to pass parameters to function.
# 4. : => colon is used to indicate the start of function body.
# 5. print("This is Suhani") => it is the content  of function.
# in c languages , we define function like this.
# function Wilmot_function() {
print("This is Suhani")

def my_function():
          print(a)

# what is function in python?
# how to define a function in python?
# how to call a function in python?
# what are advantages of function in python?
# what's the use cases of function in python?

def my_function():
    print("This is Togar")
    print("this is Ritchie")
    print("this is Cherist")


def find_square():
    my_variable = int(input("HIi, Wilmot please enter any number to find sqr: "))
    print("hii WImot here is your sqr: ",my_variable * my_variable)
find_square()
    
#first one 
def even_check(i):
    if i%2 == 0:
        print("even")
    else:
        print("odd")
v = int(input("Enter Number -> "))
even_check(v)

#second one
def even_check(a,b):
    for i in range(a,b):
        if i%2==0:
           print(i)
x=10
y=100
print(f"Even no. from {x} and {y}:- ")
even_check(x,y)