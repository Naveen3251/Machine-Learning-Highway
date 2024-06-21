'''
Abstraction is a fundamental concept in object-oriented programming that involves hiding the complex implementation 
details and showing only the necessary features of an object. 

It simplifies the complexity by providing a clear and simple interface to interact with.

NOTE:All abstract methods in the parent class must be implemented in the subclass to avoid this error
'''
from abc import ABC, abstractmethod

#parent class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

#child class 1
class Rectangle(Shape):
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def area(self):
        return self.w*self.h
    def perimeter(self):
        return 2*(self.w+self.h)
    
#child class 2
class Circle(Shape):
    def __init__(self,r):
        self.r=r

    def area(self):
        return 3.14*self.r*self.r
    
    def perimeter(self):
        return 2*3.14*self.r
    
cir=Circle(3)
print(cir.area())

rec=Rectangle(4,5)
print(rec.area())
print(rec.perimeter())