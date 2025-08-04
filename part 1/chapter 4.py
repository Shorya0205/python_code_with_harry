#Strings
## Strings are immutable in Python
a="harry"
a='harry'
a="""harry"""

#to find the length of a string
length = len(a)  # 5

#string slicing

#Positive Indexing
slice1 = a[0:3]    # 'har'
slice2 = a[1:4]    # 'arr'
char1 = a[1]       # 'a'
#Negative Indexing
slice3 = a[-4:-1]  # 'arr'
slice4 = a[-5:-2]  # 'har'
char2 = a[-4]      # 'a'

#slicing with step value
slice5 = a[0:5:2]  # 'hry'
#in this case, it starts from index 0, goes to index 5, and takes every second character

#OTHER SLICING TECHNIQUES
slice6 = a[:5]     # 'harry' as it starts from index 0 to index 5
slice7 = a[::]     # 'harry', same as a[:]
slice8 = a[0:]     #'harry' as it starts from index 0 to the end  

print(slice1, slice2, char1, slice3, slice4, char2, slice5, slice6, slice7, slice8)

#String Methods

#1. len() - returns the length of the string
length = len(a)  # 5
#2. endswith() - checks if the string ends with a specified suffix
ends_with_harry = a.endswith("ry")  # True
#3. startswith() - checks if the string starts with a specified prefix
starts_with_harry = a.startswith("ha")  # True
#4.find() - returns the lowest index of the substring if found, else returns -1
find_index = a.find("rr")  # 2
#5. capitalize() - capitalizes the first character of the string
capitalized_string = a.capitalize()  # 'Harry'
#6. count() - counts the occurrences of a substring in the string
count_h = a.count("h")  # 1
#7. replace() - replaces a substring with another substring all occurrences
replaced_string = a.replace("har", "mar")  # 'marr'
#8. isalnum() - checks if all characters in the string are alphanumeric
is_alnum = a.isalnum()  # True

#Escape sequences

# Escape sequences are used to insert characters that are illegal in a string
#To include single or double quotes in a string, you can use escape sequences
escape_string = "This is a \"double quoted\" string and this is a \'single quoted\' string"
#To include a backslash, you can use a double backslash
backslash_string = "This is a backslash: \\"
#To include a newline character, you can use \n
newline_string = "This is the first line.\nThis is the second line."
#To include a tab character, you can use \t
tab_string = "This is a tab:\tThis text is after a tab."

#wap to fill name and date in a letter template
# Template for a letter
letter_template = """Dear <NAME>,
I hope this letter finds you well. Today is <DATE> and I wanted to take a moment to reach out and say hello"""
name = input("Enter your name: ")
date = input("Enter the date: ")
print(letter_template.replace("<NAME>", name).replace("<DATE>", date))
#this is chaiining with replace method to fill the template with user input



