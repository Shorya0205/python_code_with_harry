#FILE INPUT OUTPUT


#1. OPENING A FILE
file = open("FILE.txt","r")
#2. READING A FILE
content = file.read()
#3. PRINTING THE CONTENT
print(content)
#4. CLOSING A FILE
file.close()

#READING A FILE LINE BY LINE
file = open("FILE.txt","r")
line= file.readline()
print(line)
file.close()

string = "This is a sample string"
#5. WRITING TO A FILE
file = open("FILE.txt","w")
file.write(string)
file.close()

#6.APPENDING A FILE 
file = open("FILE.txt","a")
file.write(string)
file.close()

#7. USING WITH STATEMENT
with open("FILE.txt","r") as file:
    content = file.read()
    print(content)

#8. USING WITH STATEMENT FOR WRITING
with open("FILE.txt","w") as file:
    file.write("This is a new line added to the file.\n")


#9. USING WITH STATEMENT FOR APPENDINg
with open("FILE.txt","a") as file:
    file.write("This line is appended to the file.\n")
