'''
Getters and Setters

1)When we want to avoid direct access to private variables
2)To add validation logic for setting a value

'''
class Naveen:
    def __init__(self,name,age,passcode):
        self.name=name
        self.__age=age
        self.__passcode=passcode
    
    #getters
    def get_name(self):
        return self.name
    def get_age(self):
        return self.__age
    def get_passcode(self):
        return self.__passcode
     
    #setters   
    def set_name(self,newName):
        self.name=newName
    def set_age(self,newAge):
        #condition base setting
        if newAge>=18:
            self.__age=newAge
        else:
            print("You cant set the age")
            
    def set_passcode(self,newPass):
        self.__passcode=newPass
        
obj=Naveen("Naveen",12,"12Sd90")
print(obj.get_name(),obj.get_age(),obj.get_passcode()) #op: Naveen 12 12Sd90

#again setting
obj.set_name("Kumar")
obj.set_age(19)
print(obj.get_name(),obj.get_age(),obj.get_passcode()) #Kumar 19 12Sd90
obj.set_age(14) #op: You cant set the age

