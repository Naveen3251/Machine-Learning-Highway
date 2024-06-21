#usecase for instance method
'''
A class method is a method that operates on the class itself, rather than on instances of the class.
It takes the cls parameter as the first argument, which refers to the class itself.
Class methods can access and modify class variables.
They are commonly used for factory methods or methods that need to interact with class-level data.
Class methods are defined using the @classmethod decorator.
'''
class Family:
    #class variable
    classname="Nk"
    def __init__(self,name):
        self.name=name
        
    #classmethod to change the class variable
    @classmethod
    def change(cls,newName):
        cls.classname=newName

    def show(self):
        print(self.name,Family.classname)
        
obj=Family("Naveen")
obj.show()      #op: Naveen Nk
obj.change("Kumar")
obj.show()      #op: Naveen Kumar     
