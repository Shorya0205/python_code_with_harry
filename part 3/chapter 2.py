#type definition in python
'''
age: int = 20
name: str = "Harry"
is_student: bool = True
height: float = 5.9
# type definition is not enforced in python, but it helps in understanding the code better.
# It is a way to indicate what type of data a variable should hold.
# printing the variables
print("Age:", age)
print("Name:", name)
print("Is Student:", is_student)
print("Height:", height)

#function to add two numbers
def add_numbers(a: int, b: int) -> int:
    return a + b

# calling the function
result = add_numbers(10, 20)
print("Result:", result)

#this type definitin make sure that the function only accepts integers
# and returns an integer as well.
# '''

#advance type hinting in python
'''
from typing import List, Tuple, Dict, Union

numbers= List[int] = [1, 2, 3, 4, 5]
coordinates: Tuple[float, float] = (10.0, 20.0)
person: Dict[str, Union[str, int]] = {
    "name": "Harry",
    "age": 20
}
identifier: Union[str, int] = "ID123"
# printing the advanced type hints
print("Numbers:", numbers)
print("Coordinates:", coordinates)
print("Person:", person)
print("Identifier:", identifier)
# This code demonstrates advanced type hinting in Python using the typing module.
# It shows how to use List, Tuple, Dict, and Union to define complex data structures
# with specific types for better code clarity and type checking.
# It is designed to help learners understand type hints and how they can be used
# to improve code readability and maintainability.
'''

#match case in python
'''

# The match-case statement in Python is a powerful feature introduced in Python 3.10.
# It allows for pattern matching, which can simplify complex conditional logic.
# This code demonstrates the use of match-case statements in Python, which allows
# for more readable and maintainable code by matching patterns against values.
def process_value(value):
    match value:
        case 1:
            print("Value is one.")
        case 2:
            print("Value is two.")
        case _:
            print("Value is something else.")
# Example usage of match-case
process_value(1)  # Output: Value is one.
process_value(2)  # Output: Value is two.
process_value(3)  # Output: Value is something else.

'''

#DICTIONARY COMPREHENSION AND UPDATE OPERATOR
'''# The dictionary comprehension and update operator in Python allow for concise and efficient creation and modification of dictionaries
# This code demonstrates the use of dictionary comprehension and the update operator in Python,
# which allows for more concise and efficient dictionary creation and updates.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 1, 'd': 2, 'e': 3}

merged_dict = dict1 | dict2
print("Merged Dictionary:", merged_dict)
'''
'''
#use of with statement for multiple context managers
# The 'with' statement in Python allows for the use of multiple context managers, which can
# simplify resource management and ensure proper cleanup of resources.
with open('file1.txt', 'w') as f1, open('file2.txt', 'w') as f2:
    f1.write("Hello from file 1")
    f2.write("Hello from file 2")
'''

