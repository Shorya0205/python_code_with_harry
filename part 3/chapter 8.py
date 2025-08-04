#virtual environment
#when you install a package using pip, it installs it globally
#but if you want to install it in a specific project, you can create a virtual environment
# A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python,
# along with additional packages. It allows you to manage dependencies for different projects separately.
# This code demonstrates how to create and use a virtual environment in Python.
# It shows how to create a virtual environment, activate it, and install packages within that environment
# using pip.

#isolated environment
# A virtual environment is an isolated environment that allows you to manage dependencies for a specific project without
# affecting the global Python installation. It helps avoid conflicts between different projects' dependencies.
# Example usage of creating and using a virtual environment

# To create a virtual environment, you can use the following command in your terminal:
# python -m venv myenv
# This command creates a new directory called 'myenv' that contains the virtual environment.
# To activate the virtual environment, use the following command:

# myenv\Scripts\activate

#pip freeze
# This command lists all the installed packages in the virtual environment along with their versions.

#to write the requirements.txt file
# pip freeze > requirements.txt
# This command saves the list of installed packages to a file named 'requirements.txt'.

# To install packages from a requirements.txt file, you can use the following command:
# pip install -r requirements.txt

#LAMBDA FUNCTIONS
# Lambda functions are small anonymous functions defined using the lambda keyword.
# They can take any number of arguments but can only have one expression.
# Example usage of a lambda function
'''def add(x, y):
    return x + y
# Using a lambda function to add two numbers
add_lambda = lambda x, y: x + y
# Example usage of the add_lambda function
result = add_lambda(5, 3)
print("Result of addition using lambda function:", result)

#JOIN METHOD
# The join() method is used to concatenate elements of an iterable (like a list or tuple) into a single string.
# It takes a string as a separator and joins the elements of the iterable using that separator.
def join_elements(elements, separator=", "):
    return separator.join(elements)
# Example usage of the join_elements function

elements = ["apple", "banana", "cherry"]
result = "...".join(elements)
print("Joined elements:", result)
'''
#MAP FILTER AND REDUCE
# The map() function applies a given function to all items in an iterable (like a list or tuple).
# The filter() function filters items in an iterable based on a given condition.
# The reduce() function applies a rolling computation to sequential pairs of values in an iterable.

l=[1, 2, 3, 4, 5]

squared= lambda x: x**2
squared_list = list(map(squared, l))
print("Squared list using map:", squared_list)

# Filter example
even_numbers = list(filter(lambda x: x % 2 == 0, l))
print("Even numbers using filter:", even_numbers)


def even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
only_even = list(filter(even, l))
print("Even numbers using custom function:", only_even)


#reduce function
from functools import reduce

def add(x, y):
    return x + y
sum_of_list = reduce(add, l)
print("Sum of list using reduce:", sum_of_list)