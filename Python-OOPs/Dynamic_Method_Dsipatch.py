'''
Dynamic method dispatch is the mechanism by which a call to an overridden method is resolved at runtime rather than compile-time.
'''
class Employee:
    def calculate_pay(self):
        return NotImplementedError("Subclass should implement this method")
    
class PartTime(Employee):
    def calculate_pay(self):
        return "Part time salary"
    
class FullTime(Employee):
    def calculate_pay(self):
        return "Full time salary"
    
class Intern(Employee):
    def calculate_pay(self):
        return "Stipend"


'''
Dynamic Method Dispatch: In the for employee in employees loop, the call to employee.calculate_pay() demonstrates dynamic method dispatch. Python dynamically determines which calculate_pay method to invoke based on the actual class of the object (FullTimeEmployee, PartTimeEmployee, or Contractor).
Runtime Decision: The method to be executed is decided at runtime. When employee.calculate_pay() is called, if employee is an instance of FullTimeEmployee, the calculate_pay method in FullTimeEmployee is executed. 
If employee is an instance of PartTimeEmployee, the calculate_pay method in PartTimeEmployee is executed, and so on.
'''
def salary(employess):
    for emp in employess:
        print(emp.calculate_pay())

employess=[PartTime(),FullTime(),Intern()]
salary(employess)






