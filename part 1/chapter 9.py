#if else statements

"""
if(condition):
    print("Condition is True")
    
elif(condition2):
    print("Condition 2 is True")
    
else:
  print("Both conditions are False")
    
"""

# WAP to detect spam comment keywords
#spam_keywords = ['buy now', 'click this', 'subscribe', 'make a lot of money']

p1='make a lot of money'
p2='click this'
p3='buy now'
p4='subscribe'

message = input("Enter your message: ")
if ((p1 in message) or (p2 in message) or( p3 in message) or( p4 in message)):
    print("This is a spam comment")
else:
    print("This is not a spam comment")

# WAP to find username is greater than 10 characters or not
username = input("Enter your username: ")
if len(username) > 10:
    print("Username is greater than 10 characters") 
else:
    print("Username is not greater than 10 characters")

#WAP to check harry is present in the list or not
names = ['harry', 'rohan', 'shubham', 'aman']
if ('harry' in names):
    print("Harry is present in the list")
else:
    print("Harry is not present in the list")

#WAP to check "harry" is present in the string or not
string = "This is a string containing harry"
if ("Harry".lower() in string.lower()):
    print("Harry is present in the string")
else:
    print("Harry is not present in the string")

