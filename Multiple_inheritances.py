class grandparent:
    grandparent_property="Blue Lake Place"
    def __init__(self):
        print("grandparent property")
        
        
    def show(self):
        print("grandparent show")
class parent(grandparent):
    def __init__(self):
        print("parent constructor")
    def show(self):
        print("parent show")
class child(parent):
    def __init__(self):
        print("child constructor")
    def show(self):
        print("child show")
obj=child()
obj.show()