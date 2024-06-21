#Constructor chaining 
'''
Scenario 2 
When you have multiple constructors with different parameter signatures, 
and you want to consolidate the initialization logic into a single constructor.

```
    Person (Base)
    -- have name 
        -- have name and age 
                --- have name age and gender
    In this case : name required 
                    age and gender may or may not present
'''
#parent
class Person:
    #constructor with default values
    def __init__(self,name,age=None,gender=None):
        self.name=name
        self.age=age
        self.gender=gender
    
    def show_name(self):
        print(self.name)
    
    def show_name_age(self):
        print(self.name,self.age)
    
    def show_name_age_gender(self):
        print(self.name,self.age,self.gender)

name=Person("Naveen")
name.show_name()                        #op: Naveen

name_and_age=Person("Naveen",12)
name_and_age.show_name_age()            #op: Naveen 12

name_age_gender=Person("Naveen",12,"M")
name_age_gender.show_name_age_gender()  #op: Naveen 12 M