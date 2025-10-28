sum_even = 0
prodct_odd = 1
for i in range(10, 31):
    if i % 2 == 0:
        sum_even += i
    else:
        prodct_odd *= i

print("Sum of even numbers from 10 to 30:", sum_even)
print("Product of odd numbers from 10 to 30:", prodct_odd)

string = "concatination"
print("Original string:", string)

for ch in string:
    if ch in 'aeiou':
        print(ch)


        