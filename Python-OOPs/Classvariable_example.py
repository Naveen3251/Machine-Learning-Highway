#usecase for class varibale
#You having the car company whenever a new car arrived u have to count automatically
class Car:
    car_count=0
    def __init__(self,name):
        self.name=name
        Car.car_count+=1  #whenever the new object is created it will count the new car is adding
obj1=Car("BMW")
print(obj1.car_count) #op : 1 
obj2=Car("AUDI")
print(obj2.car_count) #op : 2 

#suppose i have to change the count for obj1
#you're creating a new instance variable car_count specific to obj1, 
#so it doesn't affect the class variable or other instances.
obj1.car_count=10
print(obj1.car_count) #op: 10
print(obj2.car_count) #op: 2 
print(Car.car_count)  #op: 2 (actually two cars onlt added hence the class wi track the no of obj created)

#suppose i have to chnage the whole car count of the class
'''Car.car_count directly to 23, it modifies the class variable, 
affecting all instances. So, now obj2.car_count and Car.car_count both give 23, 
but obj1.car_count still retains the value 10, as it's a separate instance variable specific to obj1.'''
Car.car_count=23
print(obj1.car_count) #op: 10 #doesnt affect
print(obj2.car_count) #op: 23 affected
print(Car.car_count)  #op: 23