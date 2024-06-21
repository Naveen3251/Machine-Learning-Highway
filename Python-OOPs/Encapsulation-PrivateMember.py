'''
Encapsulation in Python describes the concept of bundling data and methods within a single unit.

Private Member
Private members are accessible only within the class, 
and we can’t access them directly from the class objects.

Accessible:
Through public method inside the class
'''
class Employee:
    def __init__(self,name,age):
        #instance 
        
        #public member
        self.name=name
        #private member
        self.__age=age
    
    #instance method(public method to access private member of the class)
    def show(self):
      
        print(self.name,self.__age)
        
emp=Employee("Naveen",15)

#accessing public member outside the class
print(emp.name) #op: Naveen
print(emp.__age) #op: AttributeError: 'Employee' object has no attribute '__age'
emp.show() #op: Naveen 15
