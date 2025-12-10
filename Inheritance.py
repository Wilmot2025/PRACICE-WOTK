class Father:
                   father_1st_property = "Taj Hotel"

def father_assets(self):
                           print("Bhardwaj aprament")
                           print("Willing Restaurant")


father_obj =  Father() 

# print(father_obj.father_1st_property)
# father_obj.father_assets()

class Son(Father):
    def son_assets(self):
       
# Create an instance of the Son class
            son_instance = Son()
 # Call the son_assets method
            son_instance.son_assets()
# Type of class  parent class,( base or super class
# child class (derived or sub class
#The class whos properities and mehtods are inherited is called pare

class grandson(Son):
    def grandson_assets(self):
        print("Grandson's assets")

# Create an instance of the grandson class
grandson_instance = grandson()

# Call the grandson_assets method
grandson_instance.grandson_assets()