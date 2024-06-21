'''
Polymorphism With Inheritance
Method overriding:
This process of re-implementing the inherited method in the child class is known as Method Overriding.

'''
#base class
class Vehicle:
    def speed():
       return 500
#child class     
class Car(Vehicle):
    def __init__(self,speed):
        self.speed=speed
    #overriding the method of base class
    def speed(self):
        return self.speed
car=Car(800)
print(car.speed) #op: 800
