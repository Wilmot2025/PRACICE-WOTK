for i in range(5):
    if i == 3:
        break   
    print(i)    #break is used to stop the loop when the condition is met   
# Output:

for i in range(0,10):
    if i == 8:
        break   
    print(i)    
    

for i in range(0,20,2): 
    if i == 12:
        continue
    print(i)    

for i in range(0,20,2):
    if i == 12:
        break
    print(i)

for i in range(0,20,3):
    if i == 14:
        continue
    print(i)

for i in range(0,20,4):
    if i == 16:
        break   
    print(i)    
    
    #continue is used to skip the current iteration when the condition is met

for i in range(1, 6):   
    if i == 2:
        continue  # skips printing 2
    if i == 4:
        break      # stops loop when i is 4
    print(i)

   

for item in ["apple", "banana", "bread", "orange"]:
    if item == "banana":
        continue  # skip "banana"
    if item == "bread":
        break     # stop loop when you reach "bread"
    print(item)