#if name==main


if __name__ == "__main__":
    # This block of code will only execute if the script is run directly, not if imported as a module.
    print("This script is being run directly.")


#from chapter 3 import that function 
#like this we can import the function from chapter 3
#when we import a file it will execute the code in that file
#but the code in the if __name__ == "__main__": block will not execute
# this is useful for testing code in a file without executing it when imported as a module.
#if name == "__main__": is a common Python idiom that allows you to check if a script is being run directly or imported as a module.

if __name__ == "__main__":
    print("This code is being run directly, not imported as a module.")
    print("You can run this script to see its output.")
    print("now we can use any function from chapter 3 but that will not connected to chapter 3")