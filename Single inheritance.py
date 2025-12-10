class grandFather:
     grandFather_property = "Blue Lake Place"
     def grandfather_assets(self):
         print("his property") 

class Father(grandFather):
    Father_property = "Black and white hotel"
    def father_assets(self):
        print("father hotel")

class Son(Father,grandFather):
    Son_property = "Royal Palace"
    def son_assets(self):
        print("his property")

obj_Son = Son() 
print(obj_Son.grandFather_property)
obj_Son.grandfather_assets()
print(obj_Son.Father_property)
obj_Son.father_assets()
print(obj_Son.son_property)
obj_Son.son_assets()
                  
  



         

    

  
