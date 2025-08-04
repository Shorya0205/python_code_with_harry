#practice set of file i/o

#wap to read a file and find out the given word is present in the file or not

def check_word_in_file(filename, word):
    with open(filename, 'r') as file:
        content = file.read()
        if word in content:
            print(f"The word '{word}' is present in the file.")
        else:
            print(f"The word '{word}' is not present in the file.") 

#wap to find out the number of lines in a file
def count_lines_in_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"The number of lines in the file is: {len(lines)}")

#wap to find out the number of words in a file
def count_words_in_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        print(f"The number of words in the file is: {len(words)}")

#wap to make a copy of a file
import shutil
def copy_file(source, destination):
    shutil.copy(source, destination)
    print(f"File copied from {source} to {destination}")

#wap to delete a file
import os
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' has been deleted.")
    else:
        print(f"The file '{filename}' does not exist.")

#wap to rename a file
def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}'.")
    else:
        print(f"The file '{old_name}' does not exist.")

#wap to read a file and print its content in reverse order
def print_file_content_reverse(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print("Content in reverse order:")
        print(content[::-1])


