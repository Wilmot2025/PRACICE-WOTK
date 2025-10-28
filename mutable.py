mutable_list = [1, 2, 3]
mutable_list[0] = 10  # Modifying the first element
print(mutable_list)  # Output: [10, 2, 3]

immutable_tuple = (1, 2, 3) 
# immutable_tuple[0] = 10  # This will raise a TypeError    
print(immutable_tuple)  # Output: (1, 2, 3)
# Tuples are immutable, so the following line would raise an error if uncommented   

# immutable_tuple[0] = 10   
# Output: (1, 2, 3)

mutable_list.append(4)  # Adding an element to the list
print(mutable_list)  # Output: [10, 2, 3, 4]
