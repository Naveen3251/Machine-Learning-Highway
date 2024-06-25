#Association
'''
1] It use "Use-a" Relationship

2] "Independent lifecycle" both object independently acts

3] One class obj uses other but doesn't own it
'''

class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return (self.pay*12)+self.bonus
    
class Employee:
    def __init__(self,name,exp):
        self.name=name
        self.exp=exp

    #uses the method of salay class but doesn't own
    def total_pay(self,salary):
        return salary.annual_salary()
    
obj1=Salary(1020300,980789)
obj2=Employee("Naveen",2)

#using the Salary class method in employee class without owning
print(obj2.total_pay(obj1))

'''
 Here,
  obj1 --> Salary()
  obj2 --> Employee()

  if obj2 is destroyed, obj1 remains as it is and vice versa.
  The Employee object uses the Salary object but does not own it.
'''