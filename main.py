import pyttsx3 as p
import speech_recognition as sr
import selenium_web
import pywhatkit
import randfacts
from jokes import *
from weather import *
import datetime
import googletrans
import os
import subprocess
from pynput.keyboard import Key, Controller

keyboard = Controller()

gt = googletrans.Translator()

engine = p.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate' , 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

today_date = datetime.datetime.now()
r = sr.Recognizer()

def wishme():
    hour = int(today_date.hour)
    if hour>0 and hour<12:
        return ("Morning")
    elif hour>=12 and hour<16:
        return ("Afternoon")
    else:
        return ("Evening")

speak("Press 1 for english")
inst = "Press two for Kannada"
inst = gt.translate(inst, dest="kn")
print(inst.text)
speak(inst.text)
speak("Hey! Good " + wishme())
speak("I am Linux. Your personal voice assistant. How can I help you?")


with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('Listening...')
        audio = r.listen(source)
        text = r.recognize_google(audio, language='hi-in')
        text = gt.translate(text)
        text = text.text
        print(text)
        text = text.lower()

if "information" in text:
        tell = "About what topic do you need information?"
        tell = gt.translate(tell, dest="hi")
        print(tell.text)

        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print('Listening...')
            audio = r.listen(source)
            info = r.recognize_google(audio)
        speak("Searching {} in Google".format(info))
        print("Searching {} in Google".format(info))
        assist = selenium_web.infow()
        assist.get_info(info)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

elif "play" and "video" in text:
        speak("What video do you want to play?")

        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print('Listening...')
            audio = r.listen(source)
            vid_title = r.recognize_google(audio)
        speak("Playing {} on Youtube".format(vid_title))
        print("Playing {} on Youtube".format(vid_title))
        pywhatkit.playonyt(vid_title)

elif "joke" in text:
        tell = "Sure! Here's your joke"
        tell = gt.translate(tell, dest="hi")
        print(tell.text)
        speak(tell.text)
        arr = joke()
        print(arr[0])
        speak(arr[0])
        print(arr[1])
        speak(arr[1])

elif "fact" in text:
        speak("Here's a fact for you!")
        x = randfacts.getFact()
        print(x)
        speak("Did you know that, " + x)

elif "weather" in text or "temperature" in text:
        print("The temperature today in Gulbarga is " + str(temp()) + " degree celsius with " + str(des()))
        speak("The temperature today in Gulbarga is " + str(temp()) + " degree celsius with " + str(des()))

elif "today" and "date" in text:
        speak("Today is " + today_date.strftime("%d") + " of" + today_date.strftime("%B") + " And its currently " + (today_date.strftime("%I")) +" " + (today_date.strftime("%M")) + (today_date.strftime("%p")))

elif "sublime" in text:
        speak("Opening")
        os.system("/snap/sublime-text/current/opt/sublime_text/sublime_text")

elif "open" and "chrome" in text:
        speak("Opening Chrome")
        assist = selenium_web.infow()

elif "run" and "command" in text:
        subprocess.run(["python3", "weather.py"])

elif "exit" in text:
        speak("Exiting! Bye")
        quit()