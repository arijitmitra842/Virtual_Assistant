import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
# Listener is a variable created to recognize the voice
listener = sr.Recognizer()
speak_engine = pyttsx3.init()
my_voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', my_voices[2].id)

def speak(text):
    speak_engine.say(text)
    speak_engine.runAndWait()

def follow_commands():
    try:
        with sr.Microphone() as source:
            print("Yes I am listening, Please tell....")
            my_voice = listener.listen(source)
            my_commands = listener.recognize_google(my_voice)
            if 'bob' in my_commands:
                my_commands = my_commands.replace('bob', '')
                my_commands.lower()
                print(my_commands)
    except:
        pass
    return my_commands

def run_bob():
    my_commands = follow_commands()
    print(my_commands)
    if 'play' in my_commands:
        music = my_commands.replace('play','')
        speak("Lets play" + music)
        pywhatkit.playonyt(music)
    elif 'time' in my_commands:
        time = datetime.datetime.now().strftime("%H: %M: %S")
        speak("The exact current time is" + time)
    elif 'who is' in my_commands:
        individual = my_commands.replace('Who is', '')
        data = wikipedia.summary(individual, 5)
        print(data)
        speak(data)
    elif 'coding' in my_commands:
        speak("Coding is fun")
    elif 'are you free' in my_commands:
        speak("I have a lot of work to do")
    elif 'joke' in my_commands:
        speak(pyjokes.get_joke())
    else:
        speak("I haven't understood, Can you repeat again.")
while True:
    run_bob()



