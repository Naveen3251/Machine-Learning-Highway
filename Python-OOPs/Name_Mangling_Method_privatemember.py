'''
Name Mangling to access private members

'''
class My:
    def __init__(self,name,age):
        #protected member
        self._name=name
        #private member
        self.__age=age
        
    #public method to acces protected and private member
    def show(self):
        print(self._name,self.__age)
v=My("Naveen",12)
v.show() #Naveen 12

print(v._name) #op: Naveen (bcz it is protected member only)
#print(v.__age) #op: error will arise (bcz it is private member we cant access to solve we use name Mangling)

#Name Mangling (syntax: obj._classname__privatevariable)
print(v._My__age)

