#Destructor
'''Why Destructor Might Be Called Immediately
Reference Counting:
Python uses reference counting to manage memory. An object is destroyed (and __del__ is called) when its reference count drops to zero.
Interactive Environment:
In an interactive environment, temporary references to objects might be handled differently. 
For example, the Python shell or Jupyter notebook might clean up objects immediately after their use to free up memory.
'''
class Destroy:
    def __init__(self,name):
        self.name=name
        print("Constructor called")
    def show(self):
        print(self.name)
    def __del__(self):
        print("Destructor called")
    
s1=Destroy("Devil")
s1.show()
del s1
        
