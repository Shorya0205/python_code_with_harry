#1--} Use external modules


import pyjokes
import pyttsx3
import os

#Get a random joke 
joke = pyjokes.get_joke()
print(joke)

# Speak the joke using text-to-speech
engine = pyttsx3.init()
engine.say(joke)
engine.runAndWait()

# Show contents of a directory
directory_path= '/PYTHON FILES' 
contents= os.listdir(directory_path)

for item in contents:
    print(item)