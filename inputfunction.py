irst_value = 10

second_value = 20

my_number = int(input("Hii, Sharik please enter the number: "))

if (my_number % 2 == 0):
                    print("this is even number")
else: 
                    print("this is odd number")




# print( 55 % 2 )
# print(10 % 2)   


# => we get remainder == 0 => this is even number 
# => and we don't get the remainder == 0 => this is odd number

# we can remainder by using division operation.

# my_number = 99
# my_number = int(input("enter the number"))

# if my_number > 0:
#                     print("this is Positive number")
   
# elif my_number < 0: 
#                     print("the number is Negative ")

# else:
#                     print("the number is equal to 0")



fist_name = input("enter your first name")
last_name = input("enter your last name")
full_name = fist_name + " " + last_name

print("your full name is : ", full_name)

a = 20
b = 10
c = 30

if a > b and a > c :
                    print("a is greater")

elif b > a and b > c :
                    print("b is greater")

else:
                    print("c is greater")


# NOte: and operator => it gives true if both conditions will be true, otherwise it gives false .
# OR operator => it gives true if any one condition is true, otherwise it gives false.  
age = int(input("enter your age"))
citizen = input("enter your citizenship")   
if age >= 18 and citizen.lower() == 'indian':
                    print("You are eligible to vote")
else:
                    print("You are not eligible to vote")       
age = int(input("enter your age"))
citizen = input("enter your citizenship")
if age >= 18 or citizen.lower() == 'Liberian':
                    print("You are eligible to vote")