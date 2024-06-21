#usecase for instance method
'''An instance method is a method that operates on instances of a class.
It takes the self parameter as the first argument, which refers to the instance itself.
Instance methods can access and modify instance and also class variables.'''
class Family:
    def __init__(self,name,age):
        #instance variables
        self.name=name
        self.age=age
    
    #instance methods
    #accesing instance variables inside instance method
    #to print
    def show(self):
        print(self.name,self.age)
        
    #modifying instance variables using instance method
    #to change the name and age
    def change_name(self,newName):
        self.name=newName
    def change_age(self,newAge):
        self.age=newAge
        

#object of the class
obj1=Family("Naveen",12)
obj1.show() #op: Naveen 12
#changing the name
obj1.change_name("Kumar")
obj1.show() #op: Kumar 12
#chnaging the age
obj1.change_age(19)
obj1.show() #op: Kumar 19

