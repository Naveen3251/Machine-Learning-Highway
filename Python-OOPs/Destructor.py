#Destructor

class Destroy:
    def __init__(self,name):
        self.name=name
        print("Constructor called")
    def show(self):
        print(self.name)
    def __del__(self):
        print("Destructor called")
    
s1=Destroy("Devil")
s1.show()
del s1
        
