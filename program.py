# program to write my name.
def name():
    print("My name is Wilmot T. Okai") 

# program to write enter interger and enter by the user.
number = int(input("Enter an integer: "))
print("You entered:", number)

# program to add two numbers.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
sum = a + b
print("Sum =", sum)

# program to check if a number is prime or not.
n = int(input())
print("Prime" if n>1 and all(n%i for i in range(2, int(n**0.5)+1)) else "Not Prime")


