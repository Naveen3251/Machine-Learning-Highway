#usecase for instance method
'''An instance method is a method that operates on instances of a class.
It takes the self parameter as the first argument, which refers to the instance itself.
Instance methods can access and modify instance and also class variables.'''
class Family:
    #class variable
    count=0
    def __init__(self,name,age):
        #instance variables
        self.name=name
        self.age=age
        Family.count+=1
    
    #instance methods to access class variable and instance varible
    #accesing instance variables inside instance method
    #to print
    def show(self):
        print(self.name,self.age,Family.count)
        
    #modifying class variable using instance method
    #to change the name and age
    def change_count(self,newCount):
        Family.count=newCount
        

#object of the class
obj1=Family("Naveen",12)
obj1.show() #op: Naveen 12 1
#changing the name
obj1.change_count(15)
obj1.show() #op: Naveen 12 15

obj1.show() #op: Naveen 12 15