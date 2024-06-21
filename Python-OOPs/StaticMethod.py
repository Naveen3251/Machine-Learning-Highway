#static method
'''
It is a general utility method that performs a task in isolation. 
Inside this method, we don’t use instance or class variable because this static 
method doesn’t have access to the class attributes.
[meaning:"These functions are logically related to the class but don't depend on instance or class state" means that the 
functions are conceptually associated with the class, but they don't require access 
to any specific data stored within class instances (instance state) 
or within the class itself (class state).]
'''
class Math:
    @staticmethod
    def add(x,y):
        return x+y
        
    @staticmethod
    def subtract(x,y):
        return x-y
print(Math.add(2,5))    #op: 7
print(Math.subtract(2,5)) #op: -3

