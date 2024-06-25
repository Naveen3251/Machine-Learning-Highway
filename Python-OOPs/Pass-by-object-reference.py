#Pass by object reference or Pass-by-assignment
'''
When an argument is passed to a function, the function receives a reference to the object, not the actual value or a direct reference to the variable itself. 
This means that if you pass a mutable object (like a list or a dictionary), the function can modify the original object. 
However, if you pass an immutable object (like an integer, string, or tuple), the function cannot modify the original object.
'''

# Immutable objects(Integer,String,Tuple) -- we can say as pass by value
#eg 1: Integer
def change_integer(x):
    x+=10
    print("Inside the int function",x) #20

x=10
print("Before calling function",x) #10
change_integer(x)
print("After calling function",x) #10

#eg 2: string
def change_string(s):
    s="AK"
    print("Inside string function",s) # AK

s="Naveen"
print("Before calling function",s) #Naveen
change_string(s)
print("After calling function",s) #Naveen

#Mutable objects(lists, dictionary)

#eg1 : list
def change_elements(l):
    l[0]=9
    print("Inside the  function",l) #[9,2,3,4]

lis=[1,2,3,4]
print("Before calling function",lis) #[1,2,3,4]
change_elements(lis)
print("After calling function",lis) #[9,2,3,4]

#eg2 : dictionary

def change_dic_elements(d):
    d["Name"]="Kumar"
    print("Inside the  function",d) #{'Name': 'Kumar', 'Age': 12}

dic={
    "Name":"Naveen",
    "Age":12
}

print("Before calling function",dic) #{'Name': 'Naveen', 'Age': 12}
change_dic_elements(dic)
print("After calling function",dic) # {'Name': 'Kumar', 'Age': 12}
