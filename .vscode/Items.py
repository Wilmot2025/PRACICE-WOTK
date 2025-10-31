item = ["Apple", "banana", "Orange", "grapes", "mango", "strawberry"]
print(item[1])
print(item[1:3])
print(item[-1])
print(item[-3:-1])
print(item[1:3:2])
print(item[::2])

item.append("Pineapple")
# insert multiple items at index 5 using slice assignment
item[5:5] = ["Peach", "apple", "jam", "corn", "pawpaw"]
item.remove("Peach")

