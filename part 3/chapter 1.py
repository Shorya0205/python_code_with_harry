#walrus operator

# The walrus operator (:=) allows you to assign a value to a variable as part of an expression.
# This can make your code more concise and readable by reducing the need for separate assignment statements.
# This code demonstrates the use of the walrus operator (:=) in Python, which allows 
# assignment within an expression.
# The walrus operator is useful for simplifying code by allowing you to assign a value
# to a variable and use that value in the same expression.

# Example usage of the walrus operator

'''
def process_data(data):
    if (n := len(data)) > 0:
        print(f"Processing {n} items.")
        for item in data:
            print(f"Item: {item}")
    else:
        print("No items to process.")


#example 2
if (n := len([1,2,3,4,5])) > 3:
    print(f"LIST IS TWO LONG ({n} elements , expected <=3)")

'''

# 