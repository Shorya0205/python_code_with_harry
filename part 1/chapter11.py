#Multiplication table with for loop
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Multiplication table with while loop
num = int(input("Enter a number to print its multiplication table: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

#WAP to greet all persons in a list which start with S
names = ["Harry", "Sohan", "Sachin", "Rahul"]
for name in names:
    if name.startswith("S"):
        print(f"Hello {name}, Good Morning!")
    else:
        print(f"Hello {name}, chup chap baitho!")

#WAP to print the sum of first n natural numbers
n = int(input("Enter a number to find the sum of first n natural numbers: "))
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
    print(f"The sum of first {n} natural numbers is: {sum_n}")

#wap to print pattern
#      *
#    * * *
#  * * * * *
n = int(input("Enter the number of rows for the pattern: "))
for i in range(n):
    print(" " * (n - i - 1) + "* " * (2 * i + 1))

#WAP to print the factorial of a number
num = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
    print(f"The factorial of {num} is: {factorial}")


