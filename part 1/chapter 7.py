#SETS AND DICTIONARY
#SETS ARE UNORDERED COLLECTIONS OF UNIQUE ELEMENTS AND DICTIONARIES ARE UNORDERED COLLECTIONS OF KEY-VALUE PAIRS.

#DICTIONARY
# A dictionary is a collection of key-value pairs, where each key is unique.
# It is mutable, meaning you can change its content after creation.
SAMPLE_DICT = {"name": "Alice", 
               "age": 30, 
               "city": "New York",
               list: [1, 2, 3, 4, 5]}

# print(SAMPLE_DICT[0])  # Accessing the first element (not valid, will raise KeyError)

print(SAMPLE_DICT["name"])  # Accessing the value associated with the key 'name'
print(SAMPLE_DICT["age"])  # Accessing the value associated with the key 'age'

#dictionary methods
#1. keys()
print(SAMPLE_DICT.keys())  # Getting all keys in the dictionary
#2. values()
print(SAMPLE_DICT.values())  # Getting all values in the dictionary
#3. items()
print(SAMPLE_DICT.items())  # Getting all key-value pairs in the dictionary
#4. get()
print(SAMPLE_DICT.get("city"))  # Getting the value associated with the key 'city'
#5. pop()
print(SAMPLE_DICT.pop("age"))  # Removing the key 'age' and returning its value
#6. update()
SAMPLE_DICT.update({"country": "USA"})  # Adding a new key-value pair
print(SAMPLE_DICT)  # Printing the updated dictionary
#7. clear()
SAMPLE_DICT.clear()  # Removing all items from the dictionary
print(SAMPLE_DICT)  # Printing the cleared dictionary
#8. len()
print(len(SAMPLE_DICT))  # Getting the number of key-value pairs in the dictionary

#difference between 'get ' and '[]'
# The 'get' method returns None if the key does not exist, while using '[]' raises a KeyError.
