#List and tuples

#LIST IS mutable AND TUPLE IS IMMUTABLE
#list CAN STORE DIFFERENT DATA TYPES BUT TUPLE CAN STORE ONLY SAME DATA TYPES

#LIST
SAMPLE_LIST = [1, 'python', 3.14, True]
print(SAMPLE_LIST)
print(SAMPLE_LIST[0])  # Accessing the first element

SAMPLE_LIST[0] = 'changed'  # Modifying the first element
print(SAMPLE_LIST)
print(SAMPLE_LIST[0])  # Accessing the first element again
#list slicing is same as string slicing

#LIST METHODS

#1. append()
SAMPLE_LIST.append('new item')  # Adding a new item to the end of the list
#2.INSERT()
SAMPLE_LIST.insert(1, 'inserted item')  # Inserting an item at index 1
#3.remove()
SAMPLE_LIST.remove('python')  # Removing the first occurrence of 'python'
#4.pop()
SAMPLE_LIST.pop()  # Removing the last item and returning it
#5.sort()
SAMPLE_LIST.sort()  # Sorting the list in ascending
#6.reverse()
SAMPLE_LIST.reverse()  # Reversing the order of the list
#7.clear()
SAMPLE_LIST.clear()  # Removing all items from the list
print(SAMPLE_LIST)  # Printing the modified list

#DIFFERENCE BETWEEN LIST AND STRINGS ARE THAT STRINGS ARE IMMUTABLE AND LISTS ARE MUTABLE.