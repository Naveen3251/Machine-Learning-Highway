#Composition

'''
1] It form "Part-of" relationships

2] It has dependent life cycle

3] The lifecycle of the part is tightly bound to the lifecycle of the whole. If the whole is destroyed, the part is also destroyed.

'''

class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return (12*self.pay)+self.bonus

class Employee:
    def __init__(self,name,exp,pay,bonus):
        self.name=name
        self.exp=exp
        self.obj_salary=Salary(pay,bonus)

    def total_pay(self):
        return self.obj_salary.annual_salary()
    
emp=Employee("Naveen",2,5678900,67890)
print(emp.total_pay())

'''
 Here,
  Salary is Part-of Employee
  
  if emp(whole) deleted the Salary(part) automatically deleted
'''