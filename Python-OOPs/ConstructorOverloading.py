#Constructor overloading --not supported in python
'''
Constructor overloading is a concept of having more than one constructor 
with a different parameters list in such a way so that each constructor can perform different tasks.
'''
class Construct:
    #constructor 1 with 1 agrs  
    def __init__(self,name):
        self.name=name
        print(self.name)
        
    #constructor 2 with 2 agrs 
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
       
#in python it always look for last constructor out of n constructor it does not excute based on matching of agrs 
#instead it default execute last

obj=Construct("Naveen") #TypeError: Construct.__init__() missing 1 required positional argument: 'age'

obj2=Construct("Naveen",12) #op: Naveen 12


