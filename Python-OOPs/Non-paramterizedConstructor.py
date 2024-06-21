#Non-Parametrized Constructor
'''
A constructor without any arguments is called a non-parameterized constructor. 
This type of constructor is used to initialize each object with default values.
'''
class Construct:
    #no paramter is taken hence,
    #it is non-parameterized constructor   
    def __init__(self):
        self.name="Naveen"
        self.age=10
        print("Executed at the time of object creation") #this is executed at the time of obj created
    #instance method
    def show(self):
        print(self.name,self.age)

obj=Construct()  #op: Executed at the time of object creation
obj.show()  #op: Naveen 10

