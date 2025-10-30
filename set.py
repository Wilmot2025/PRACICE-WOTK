set= (jones, "Doe", 42, "jones@example.com")        
print(set)
print(type(set))    

set = {1, 2, 3, 4, 5}       

print(set)
print(type(set))
#Set Methods
set.add(6)      
print(set)

set.remove(3)   
print(set)  
set.discard(10)  
print(set)
set.pop()
print(set)
set.clear()
print(set)  
del set 
"#Output:
('jones', 'Doe', 42, 'jones@example.com')
<class 'tuple'>     
{1, 2, 3, 4, 5}
<class 'set'>
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5}
set()       

# set intersection, union, and difference operations can also be performed using methods like .intersection(), .union(), and .difference().   
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6} 
intersection = setA & setB  
print(intersection)