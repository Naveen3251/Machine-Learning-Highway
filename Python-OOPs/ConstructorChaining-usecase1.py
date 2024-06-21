#Constructor chaining 
'''
Scenario 1 
When you have a base class with common initialization logic that should be executed 
regardless of which constructor is called.
'''
#parent base class this property is common for all vechicle types
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

#vechicle1-car
class Car(Vehicle):
    def __init__(self,make,model,year,num_of_doors):
        #invoke the base class contructor property
        super().__init__(make,model,year)
        self.num_of_doors=num_of_doors
        print(self.make,self.model,self.year,self.num_of_doors)

#vehicle2-Bike
class Bike(Vehicle):
    def __init__(self,make,model,year,engine_capacity):
        super().__init__(make,model,year)
        self.engine_capacity=engine_capacity
        print(self.make,self.model,self.year,self.engine_capacity)
        
car=Car("Toyota", "Corolla", 2022, 4) #op: Toyota Corolla 2022 4
bike=Bike("BMW","x-1ZM",2023,"100hp") #op: BMW x-1ZM 2023 100hp

        