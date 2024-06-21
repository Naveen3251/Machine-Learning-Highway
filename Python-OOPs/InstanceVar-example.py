#usecase for instance varibale
'''Instance variables are used when you need to store data that is unique to each instance of a class. 
They are properties that are specific to an object created from the class.'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age 
    def show(self):
        print(self.name,self.age)
#instace are created
obj1=Person("NAVEEN",12)
obj2=Person("KUMAR",15)
obj1.show() #op1 : NAVEEN 12
obj2.show() #op2 : KUMAR 15

