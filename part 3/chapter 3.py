#try and except block
try:
    a = 10
    b = 0
    c = a / b
    print("Division successful, result is:", c)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except TypeError:
    print("Error: Invalid type for division.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
except:
    print("An unknown error occurred.")
else:
    print("No errors occurred, division was successful.")

# if the try block executes without any exceptions, the else block will execute.
finally:
    print("Execution of try-except block is complete.")

# finally block
# The finally block will always execute, regardless of whether an exception occurred or not.
#the main purpose of finally is to execute code that must run whether an exception occurred or not, such as cleanup actions.
#mosty used in function even if we return it doesnt stop the execution of finally block.


# This code demonstrates the use of try and except blocks to handle exceptions in Python.
# It attempts to divide two numbers and catches specific exceptions like ZeroDivisionError and TypeError.
# The code also includes a general exception handler to catch any other unexpected errors.
# The try block contains code that may raise an exception.
# The except blocks handle specific exceptions and print appropriate error messages.
# The code is designed to prevent the program from crashing due to unhandled exceptions.
# The try-except structure allows for graceful error handling and debugging.
# The code is useful for learning how to manage errors in Python programs effectively.
# The code is a simple demonstration of exception handling in Python.

#error rasing
def divide_numbers(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

try:
    result = divide_numbers(10, 0)
    print("Result:", result)
except ValueError as ve:
    print("Caught an error:", ve)
# This code defines a function that divides two numbers and raises an error if the second number is zero.
# It then attempts to call this function and catches the ValueError if it occurs.