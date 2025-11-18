# Identity operator : # => it is use for address of elements not the elements.
# it compares the address of elements not the values or elements.
suhani_list = [ 1, 2, 3, 4, 5 ]
suhani_list1 = [ 1, 2, 3, 4, 5 ]    
print ( suhani_list is suhani_list1 ) # False
print ( suhani_list == suhani_list1 ) # True

# is operator is use for identity operator.
# == operator is use for equality operator.

togar_list = [ 1111, 2333, 443, 455, 6665 ] 
togar_list1 = togar_list    
print ( togar_list is togar_list1 ) # True

uhani_list = [ 1111, 2333, 443, 455, 6665 ]
print(suhani_list)

nisha_list = suhani_list
print("nisha list : ", nisha_list)
print(suhani_list is nisha_list)  # true


