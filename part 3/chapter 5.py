#enumerate function

# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
# This is useful when you need a counter with the values from the iterable.

# Example usage of enumerate()
'''
def process_items(items):
    for index, item in enumerate(items):
        print(f"Item IS AT {index} AND ITEM IS  {item}")
# Example usage of the process_items function
items = ['apple', 'banana', 'cherry']
process_items(items)    
# This code demonstrates the use of the enumerate() function to iterate over a list of items
# while keeping track of their indices. It prints each item along with its index in the list
# The enumerate function is useful for iterating over a list while keeping track of the index of each item.
# This code defines a function that processes a list of items and prints each item with its index.
# The enumerate function is a built-in Python function that allows you to loop over an iterable
# while keeping track of the index of each item. It returns an enumerate object that contains pairs
# of index and value from the original iterable.

#TO MAKE IT EASY

'''

#LIST COMPREHENSION
# List comprehension is a concise way to create lists in Python.
# It allows you to generate a new list by applying an expression to each item in an existing iterable.
# Example usage of list comprehension
#TO MAKE NEW LIST BY EXISTING LIST
mylist = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in mylist]
print(squared_list)  # Output: [1, 4, 9, 16, 25]

#Othrwise this was the manual way
sqlist=[]
for item in mylist:
    sqlist.append(item**2)
# This code demonstrates the use of list comprehension to create a new list by squaring each element in an existing list.
# List comprehension is a powerful feature in Python that allows you to create lists in a more concise and readable way.

