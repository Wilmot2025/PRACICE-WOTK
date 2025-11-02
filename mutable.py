mutable_list = [1, 2, 3]  # Creating a list
print(mutable_list)  # Output: [1, 2, 3]

immutable_tuple = (1, 2, 3)  # Creating a tuple
print(immutable_tuple)  # Output: (1, 2, 3)
# Lists are mutable, so we can change their contents
# Tuples are immutable, so we cannot change their contents
# Lists are defined using square brackets [], while tuples use parentheses ()

imutable_list = ["apple", "bread", "watermelon", "soap", "oil"]   
print(mutable_list)

imutable_list.append("milk")  # Adding an element to the list
print(mutable_list)  # Output: ['apple', 'bread', 'watermelon', 'soap', 'oil', 'milk']
 

immutable_tuple = (1, 2, 3) 
# immutable_tuple[0] = 10  # This will raise a TypeError    
print(immutable_tuple)  # Output: (1, 2, 3)
# Tuples are immutable, so the following line would raise an error if uncommented   

# immutable_tuple[0] = 10   
# Output: (1, 2, 3)

mutable_list.append(4)  # Adding an element to the list 
print(mutable_list)  # Output: [10, 2, 3, 4]    
# Tuples do not have an append method, so the following line would raise an error if uncommented   
# immutable_tuple.append(4)
# Output: (1, 2, 3) 

mutable_list.remove(2)  # Removing an element from the list 
print(mutable_list)  # Output: [10, 3, 4]   
# Tuples do not have a remove method, so the following line would raise an error if uncommented

# Lists are mutable, so we can change their contents    
# Tuples are immutable, so we cannot change their contents  
# Lists can be modified, tuples cannot
# Lists are defined using square brackets [], while tuples use parentheses ()
# Lists are mutable, tuples are immutable

# Summary:
# Lists are mutable and can be changed after creation, while tuples are immutable and cannot be changed.
immutable_tuple = (1, 2, 3) 
# immutable_tuple[0] = 10  # This will raise a TypeError


