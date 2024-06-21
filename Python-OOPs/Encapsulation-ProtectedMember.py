'''
Encapsulation in Python describes the concept of bundling data and methods within a single unit.

Protected Member
Protected members are accessible within the class and also available to its sub-classes.

'''
#base class
class Company:
    def __init__(self,project):
        #protected member
        self._project=project
    
#child class
class Employee(Company):
    
    def __init__(self,project,cost):
        #inherit the constructor of base class
        super().__init__(project)
        self.cost=cost
        
        
    #instance method
    def show(self):
        print("Cost:",self.cost)
        #accesing the protected member of base class in the child class
        print("Project:",self._project)
        


emp1=Employee("Dhasarath",1000)
emp1.show()
# Direct access protected data member
print(emp1._project)
