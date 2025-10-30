dict_data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "painting", "swimming"],
    "occupation": "Engineer"
}


print(dict_data)


#Dictionary Methods
print(dict_data.keys())
print(dict_data.values())   
print(dict_data.items())
print(dict_data.get("name"))
print(dict_data.get("gender"))

dict_data["age"] = 31
dict_data["gender"] = " Male

#dictionary Comprehension
new_dict = {x: x**2 for x in range(1, 6)}}
print(new_dict)     
print(dict_data)
print(dict_data)

#Removing Items
removed_item = dict_data.pop("city")    
print(removed_item)
print(dict_data)        

removed_item = dict_data.popitem()    
print(removed_item) 
print(dict_data)    

del dict_data["hobbies"]
print(dict_data)


dict_data.clear()
print(dict_data)    
del dict_data


#Output:
{'name': 'John', 'age': 30, 'city': 'New York',
    'hobbies': ['reading', 'painting', 'swimming'], 'occupation': 'Engineer'}
dict_keys(['name', 'age', 'city', 'hobbies', 'occupation'])
dict_values(['John', 30, 'New York', ['reading', 'painting', 'swimming'], 'Engineer'])
dict_items([('name', 'John'), ('age', 30), ('city', 'New York'), ('hobbies', ['reading', 'painting', 'swimming']), ('occupation', 'Engineer')])"
John    

    # method returns None if key not found
None
