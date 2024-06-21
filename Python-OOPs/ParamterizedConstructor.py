#Parametrized Constructor
'''
A constructor with defined parameters or arguments is called a parameterized constructor. 
We can pass different values to each object at the time of creation using a parameterized constructor.
'''
class Construct:
    #paramter is taken hence,
    #parameterized constructor   
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Executed at the time of object creation") #this is executed at the time of obj created
    #instance method
    def show(self):
        print(self.name,self.age)

obj=Construct("Naveen",10)  #op: Executed at the time of object creation
obj.show()  #op: Naveen 10
newobj=Construct("Kumar",12) #op: Executed at the time of object creation
newobj.show() #op: Kumar 12

