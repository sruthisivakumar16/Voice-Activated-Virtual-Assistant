import pyttsx3 as p #text-to-speech
import speech_recognition as sr
from sel import *

#initiating the pyttsx3 library
engine = p.init()

#setting up the speed and voice
rate = engine.getProperty('rate')
engine.setProperty('rate',170)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello, I'm Daphne! Your Virtual Assistant! How may I help you?")

#retrieve audio from microphone
r = sr.Recognizer()


with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Go ahead, I'm listening...")
    audio = r.listen(source)
    command = r.recognize_google(audio,language='en-IN')
    print(command)

if "Google" in command:
    speak("What do you want me to google?")

    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Go ahead, I'm listening...")
        audio = r.listen(source)
        query = r.recognize_google(audio,language='en-IN',show_all = True)

    assist = infow()
    assist.get_info(query)
