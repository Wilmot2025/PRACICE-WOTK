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

    
    #continue is used to skip the current iteration when the condition is met