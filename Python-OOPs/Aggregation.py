#Aggregation
'''
1] It form "has-a" relationship between objects

2] Both objects has "Independent Lifecycle"

3] If one destroyed other doesn't destroy

'''
#example
class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def annual_salary(self):
        return (self.pay*12)+self.bonus

class Employee:
    def __init__(self,name,exp,salary):
        self.name=name
        self.exp=exp
        self.obj_salary=salary

    def total_pay(self):
        return self.obj_salary.annual_salary()
    
obj1=Salary(1000000,345678)
obj2=Employee("Naveen",2,obj1)

print("Total Pay : ",obj2.total_pay())

'''
 Here,
  obj1--> Salary()
  obj2--> Employee()

  if obj2 destroyes obj1 remains as it is and vice versa

'''