def avg():
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    c= int(input("Enter third number: "))
    d= int(input("Enter fourth number: "))
    e= int(input("Enter fifth number: "))
    average = (a + b + c + d + e) / 5
    print("The average of the five numbers is:", average)

avg()

def goodday(name):
    print("Good day, " + name + "!")

name = input("Enter your name: ")
goodday(name)


def add(a, b):
    return a + b

#FUNCTION WITH DEFAULT ARGUMENTS
def add_with_default(a, b=5):
    print (a + b)

add_with_default(10)

# ****
# ***
# **
# *



    