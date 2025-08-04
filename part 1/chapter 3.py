#Input value 

a= input("Enter a value: ")
b= input("Enter another value: ")

print("The value of a is", a)
print("The value of b is", b)
print("the value of a+b is", a+b)

#Here is the catch: a and b are strings, so a+b will concatenate them instead of adding numerically
#we can also see the type of a and b
print("The type of a is", type(a))
print("The type of b is", type(b))

#So to add them numerically, we need to convert them to integers or floats,TYPEcasting
a = int(a)
b = int(b)
print("The value of a+b is", a+b)


