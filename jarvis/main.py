import speech_recognition as sr
import webbrowser
import pyttsx3
from music import music 
import requests
import google.generativeai as genai



genai.configure(api_key="AIzaSyAQoD823hPvnJSz3obqW8CSIB6VLVdKlk")
recognizer = sr.Recognizer()
engine = pyttsx3.init()
apikey="6e0714fcc4e14a0a9b005f947e8cdd72"

def speak(text):
    print(f"SPEAK: {text}")  # Debug print
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    command = command.lower()
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "news" in command.lower():
        speak("Fetching the latest news headlines.")
        url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=6e0714fcc4e14a0a9b005f947e8cdd76"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()    
            articles = data.get("articles", [])
            if articles:
                speak("Here are the top headlines:")
                for i, article in enumerate(articles[:5], 1):  # Get top 5 headlines
                    headline = article.get("title", "No title")
                    print(f"{i}. {headline}")
                    speak(headline)
            else:
                speak("Sorry, I couldn't find any news articles.")
        else:
            speak("Failed to fetch news. Please check your API key or internet connection.")
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open stack overflow" in command:
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")
        

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "search for" in command:
        query = command.replace("search for", "").strip()
        if query:
            speak(f"Searching for {query} on Google")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("Please specify what you want to search for.")

    elif "what is your name" in command:
        speak("I am Jarvis, your personal assistant.")

    elif "how are you" in command:
        speak("I am just a program, but thank you for asking! How can I assist you today?")
    elif "tell me a joke" in command:
        speak("Why did the computer go to the doctor? Because it had a virus!")

    elif command.lower().startswith("play"):
        song = command.lower().replace("play", "", 1).strip()
        if song in music:
            speak(f"Playing {song}") 
            webbrowser.open(music[song])
        else:
            speak("Sorry, I don't have that song.")

    else:
        # let ai handle that
        try:
            prompt = (
                "You are Jarvis, a helpful voice assistant. "
                "you are a virtual assistant that can answer questions, and i m using you as a voice assistant. " \
                "You can answer questions about various topics, provide information, and assist with tasks. " \
                "If the user asks about music, provide a link to the song if available in the music dictionary.\n" \
                "If the user asks about news, provide the latest news headlines.\n" \
                "If the user asks about opening websites, open the specified website.\n" \
                "If the user asks about your name, respond with 'I am Jarvis, your personal assistant.'\n" \
                "If the user asks about your well-being, respond with 'I am just a program, but thank you for asking! How can I assist you today?'\n" \
                "If the user asks for a joke, tell a joke.\n" \
                "If the user asks to play a song, check if the song is in the music dictionary and provide the link.\n" \
                "If the user asks for a weather update, provide the current weather information.\n" \
                "If the user asks for a math problem to be solved, provide the solution.\n" \
                "If the user asks for a programming question, provide a code snippet or explanation.\n" \
                "If the user asks for a science question, provide a brief explanation or relevant information.\n" \
                "If the user asks for a history question, provide a concise summary or key facts.\n" \
                "examples like google assistant, siri, alexa, cortana, jarvis, etc.\n" \
                "If the user asks something else, answer as best as you can.\n"
                "Here is the command from the user: " +
                "try to give a helpful response based on the command and try to give in little short.\n" +
                f"User: {command}"
            )
            model = genai.GenerativeModel('gemini-2.0-flash')
            response = model.generate_content(prompt)
            answer = response.text
            print("AI:", answer)
            speak(answer)
        except Exception as e:
            print("AI error:", e)
            speak("Sorry, I couldn't get a response from Gemini AI.")


if __name__ == "__main__":
    speak("INITIALIZING JARVIS")

    while True:
        r = sr.Recognizer()
        try:
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source, timeout=3, phrase_time_limit=3)
                print("Recognizing...")
                word = r.recognize_google(audio)
                print(f"You said: {word}")
            except Exception:
                print("Could not recognize your wake word by voice. Please type 'hi' or 'hello' to start:")
                speak("Could not recognize your wake word by voice.")
                word = input("Type wake word: ")

            # Clean up the recognized word and check for common greetings
            word_clean = word.lower().strip()
            greetings = ["hi", "hey", "hello", "hay", "hello there", "hi there", "hiii", "haay"]
            if any(greet in word_clean for greet in greetings):
                speak("Yes, how can I assist you?")

                # listen for a command
                try:
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        r.adjust_for_ambient_noise(source, duration=0.5)
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")
                except Exception:
                    print("Could not recognize your command by voice. Please type your command:")
                    speak("Could not recognize your command by voice. Please type your command:")
                    command = input("Type your command: ")
                process_command(command)
            else:
                speak("I didn't catch that. Please say 'hi' or 'hello' to start a conversation.")

        except sr.UnknownValueError:
            print("Could not understand audio, please try again.")
         
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
           
        except sr.WaitTimeoutError:
            print("Listening timeout, no speech detected.")
           
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


           
            



