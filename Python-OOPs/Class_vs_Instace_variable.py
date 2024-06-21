class Car:
    #class variable
    class_variable="The brand AUDI launch"
    def __init__(self,name,model):
        #instance variable
        self.name=name
        self.model=model
    
obj=Car('Audi','XZ45')
#accessing instance variable
print("Name:",obj.name," Model:",obj.model)
#accesing class class_variable
print(obj.class_variable)
#or
print(Car.class_variable)

#changing the class variable
#only through Classname directly
Car.class_variable="The AUDI"
print(Car.class_variable) #op: The AUDI
print(obj.class_variable) #op: The AUDI
#if we change using obj
obj.class_variable="The brand"
print(obj.class_variable) #op: The brand
print(Car.class_variable) #op: The AUDI (didnt chnage globally when we use obj to change the data)