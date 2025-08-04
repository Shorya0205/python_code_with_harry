#TUPLES 
# Tuples are immutable sequences in Python, similar to lists but cannot be changed after creation.
# They can store different data types, just like lists.
#TUPLE OF ONE ELEMENT
SAMPLE_TUPLE = (100)  # This is not a tuple, it's an int
print(type(SAMPLE_TUPLE))  # Output: <class 'int'>
SAMPLE_TUPLE = (100,)  # Correct way to define a tuple with one element
print(type(SAMPLE_TUPLE))  # Output: <class 'tuple'>
SAMPLE_TUPLE2= (1, False, 3.14, 'python')  # A tuple with mixed data types
print(SAMPLE_TUPLE2)
print(SAMPLE_TUPLE2[0])  # Accessing the first element of the tuple
# Tuples do not have methods like append, insert, or remove since they are immutable.
# However, you can access elements and slice tuples like lists.
# Tuples can be sliced like lists
#1. count()
print(SAMPLE_TUPLE2.count(3.14))  # Counting occurrences of 3.14 in the tuple
#2. index()
print(SAMPLE_TUPLE2.index('python'))  # Finding the index of 'python' in the tuple
#3. len()
print(len(SAMPLE_TUPLE2))  # Getting the length of the tuple
#4. max()
print(max(SAMPLE_TUPLE2))  # Finding the maximum value in the tuple
#5. min()
print(min(SAMPLE_TUPLE2))  # Finding the minimum value in the tuple
#6.sum()
list_for_sum = (1, 2, 3, 4)
print(sum(list_for_sum))  # Summing the elements of the tuple
# Printing the final state of the tuple
print(SAMPLE_TUPLE2)  # Printing the tuple
# Tuples are often used for fixed collections of items, where immutability is desired.
#operations
#1. Concatenation
SAMPLE_TUPLE3 = SAMPLE_TUPLE2 + (5, 6)  # Concatenating another tuple
print(SAMPLE_TUPLE3)  # Output: (1, False, 3.14, 'python', 5, 6)
#2. Repetition
SAMPLE_TUPLE4 = SAMPLE_TUPLE2 * 2  # Repeating the tuple
print(SAMPLE_TUPLE4)  # Output: (1, False, 3.14, 'python', 1, False, 3.14, 'python')
#3. Membership
print(3.14 in SAMPLE_TUPLE2)  # Checking if 3.14 is in the tuple, Output: True
#4. Iteration
for item in SAMPLE_TUPLE2:
    print(item)  # Iterating through the tuple and printing each item
#5. Unpacking
a, b, c, d = SAMPLE_TUPLE2  # Unpacking the tuple into variables
print(a, b, c, d)  # Output: 1 False 3.14 python