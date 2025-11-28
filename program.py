#Program to Print Your Own Name in Python
def name():
    print("My name is Wilmot T. Okai")
name()
 
#Program to Print an Integer Entered By the User
def integer():
    num = int(input("Enter an integer: "))
    print("You entered:", num)
    integer()

# Program to Add Two Numbers
def add():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    sum_result = a + b
    print("Sum =", sum_result)

#Program to Check Whether a Number is Prime or Not
    n = int(input("Enter a number: "))
    if n > 1 and all(n % i != 0 for i in range(2, n)):
        print("Prime")
    else:
        print("Not prime")






