perso = ("jones", "Doe", 42, "jones@example.com")
print("Person Tuple:", perso)
print(type(perso))

my_set = {1, 2, 3, 4, 5}

print(my_set)
print(type(my_set))
# Set Methods
my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)
my_set.discard(10)
print(my_set)
my_set.pop()
print(my_set)
my_set.clear()
print(my_set)
del my_set
# Output (for reference):
# ('jones', 'Doe', 42, 'jones@example.com')
# <class 'tuple'>
# {1, 2, 3, 4, 5}
# <class 'set'>
# {1, 2, 3, 4, 5, 6}
# {1, 2, 3, 4, 5, 6}
# {1, 2, 3, 4, 5, 6}
# {1, 2, 3, 4, 5, 6}
# {1, 2, 3, 4, 5}
# set()

# set intersection, union, and difference operations can also be performed using methods like .intersection(), .union(), and .difference().
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
intersection = setA & setB
print(intersection)
union = setA | setB
print(union)
difference = setA - setB
print(difference)
# Output:
# {3, 4}
# {1, 2, 3, 4, 5, 6}
# {1, 2}

# set comprehension
squared_set = {x**2 for x in range(1, 6)}
print(squared_set)
# Output:
# {1, 4, 9, 16, 25}
# frozenset
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)
print(type(frozen_set))
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)           
print(type(frozen_set))












