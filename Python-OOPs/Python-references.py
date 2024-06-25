
# eg 1: mutable object(list)
l=[1,2,3,4]
print('l',l)
## m reference to l
m=l
#ids
print("Id of L",id(l)) #addres reference
print("Id of m",id(m)) #addres reference

#check both are having same values
print(m==l) #True

#check both have same reference id
print(m is l) #True
print(l is m) #True

# m is l also know as
print(id(m)==id(l)) #True

#creating copy of l and reference to other object
l_copy=l.copy()
print("Id of l",id(l)) #addres reference
print('Id of l_copy',id(l_copy)) #addres reference

print("l==l_copy", l==l_copy) #True

print("l and l_copy id are same?",id(l)==id(l_copy)) #False


#eg 2: for immutable object (tuple)

a=(1,2,3)
b=a

#checking both are same references
print("Id of a",id(a))  #Id of a 1696638890560
print("Id of b",id(b))  #Id of a 1696638890560


print("References of a and b same?",id(a)==id(b)) #True
print(a is b) #True
print(b is a) #True
#both are having same elements
print("a and b contains same elemets",a==b) #True

#eg 3: integer
k=0
j=k
print(id(k)==id(j)) #True