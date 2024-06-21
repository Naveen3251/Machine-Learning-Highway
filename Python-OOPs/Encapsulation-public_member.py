'''
Encapsulation in Python describes the concept of bundling data and methods within a single unit.
Public Member
Public data members are accessible within and outside of a class. 
All member variables of the class are by default public.
'''
class Employee:
    def __init__(self,name,age):
        #instance 
        #public member
        self.name=name
        self.age=age
    
    #instance method
    def show(self):
        #accessing public member within the class
        print(self.name,self.age)
        
emp=Employee("Naveen",15)

#accessing public member outside the class
print(emp.name,emp.age) #op: Naveen 15
emp.show() #op: Naveen 15
