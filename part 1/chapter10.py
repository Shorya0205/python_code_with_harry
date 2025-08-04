#LOOPS IN PYTHON

# for loop [start stop step]


# for loop with a range
for i in range(10):
    print(i)

# for loop with a range starting from 1
for i in range(1, 11):
    print(i)

# for loop with a step
for i in range(0, 10, 2):
    print(i)

# for loop with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# for loop with a string
for char in "hello":
    print(char)

#for loop with else
# for loop with else
for i in range(5): 
    print(i)
else:
    print("Loop completed successfully.")

# for loop with a pass statement
for i in range(5):
    if i == 2:
        pass  # do nothing when i is 2
    print(i)

#DIFFERNCE BETWEEN THE PASS AND CONTINUE STATEMENT
# The 'pass' statement does nothing and is used as a placeholder,
# while the 'continue' statement skips the current iteration and moves to the next one.


# while loop


# while loop example
count = 0   
while count < 5:
    print(count)
    count += 1  # increment the count by 1 each time

# while loop with a condition
number = 10
while number > 0:
    print(number)
    number -= 1  # decrement the number by 1 each time

# while loop with a break statement
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break  # exit the loop if user types 'exit'
    else:
        print(f"You typed: {user_input}")

# while loop with a continue statement
count = 0
while count < 5:
    count += 1  # increment the count by 1 each time
    if count == 3:
        continue  # skip the rest of the loop when count is 3
    print(count)  # this will not print when count is 3

# while loop with printing list elements
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1  # increment the i by 1 each time

