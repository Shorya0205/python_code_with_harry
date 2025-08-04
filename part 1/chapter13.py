#RECURSION

# This function calculates the factorial of a number using recursion.
n= int(input("Enter a number to calculate its factorial: "))
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of {n} is:", factorial(n))
    