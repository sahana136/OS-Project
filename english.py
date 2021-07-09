import pyttsx3 as p
import speech_recognition as sr
import selenium_web
import pywhatkit
import randfacts
from jokes import *
from weather import *
import datetime
import googletrans
import subprocess
import tkinter as tk
from tkinter import *
import os
import GUI
import time

gt = googletrans.Translator()

r = sr.Recognizer()

engine = p.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate' , 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

today_date = datetime.datetime.now()

#while True:

#    root.update_idletasks()
#    root.update()

def wishme():
    hour = int(today_date.hour)
    if hour>0 and hour<12:
        return ("Morning")
    elif hour>=12 and hour<16:
        return ("Afternoon")
    else:
        return ("Evening")

def wish():
    #GUI.T.insert(INSERT,
    #             "\nLINUX VA: Hey! Good " + wishme() + "I am Linux. Your personal voice assistant. How can I help you?")
    #GUI.root.update_idletasks()
    #GUI.root.update()
    text = "Hey! Good " + wishme() + ". I am Linux. Your personal voice assistant. How can I help you?"
    GUI.shortener("\n\nLINUX VA: " + text)
    #speak("Hey! Good " + wishme())
    #speak("I am Linux. Your personal voice assistant. How can I help you?")
    speak(text)

def assistant():
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('Listening...')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            GUI.shortener("\n\nUSER: " + text)
            print(text)
            text = text.lower()
        except LookupError:
            text = "Could not understand what you said. Can you please repeat?";
            GUI.shortener(text);
            print(text);

    if "information" in text:
        tell = "About what topic do you need information?"
        GUI.shortener("\n\nLINUX VA: " + tell)
        print(tell)
        speak(tell)

        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print('Listening...')
            audio = r.listen(source)
            info = r.recognize_google(audio)
        GUI.shortener("\n\nLINUX VA: " + "Searching {} in Google".format(info))
        speak("Searching {} in Google".format(info))
        print("Searching {} in Google".format(info))
        assist = selenium_web.infow()
        assist.get_info(info)
        time.sleep(5)

    elif "play" and "video" in text:
        GUI.shortener("\n\nLINUX VA: What video do you want to play?")
        print("What video do you want to play?")
        speak("What video do you want to play?")

        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print('Listening...')
            audio = r.listen(source)
            text = r.recognize_google(audio)
            vid_title = r.recognize_google(audio)
        GUI.shortener("\n\nUSER: " + text)
        GUI.shortener("\n\nLINUX VA: " + "Playing {} on Youtube".format(vid_title))
        speak("Playing {} on Youtube".format(vid_title))
        print("Playing {} on Youtube".format(vid_title))
        pywhatkit.playonyt(vid_title)
        time.sleep(7)

    elif "joke" in text:
        tell = "Sure! Here's your joke."
        GUI.shortener("\n\nLINUX VA: " + tell)
        print(tell)
        speak(tell)
        arr = joke()
        GUI.shortener("\n\nLINUX VA: " + arr[0])
        print(arr[0])
        speak(arr[0])
        GUI.shortener("\n\nLINUX VA: " + arr[1])
        print(arr[1])
        speak(arr[1])

    elif "fact" in text:
        speak("Here's a fact for you!")
        x = randfacts.getFact()
        GUI.shortener("\n\nLINUX VA: " + "Here's a fact for you")
        print(x)
        GUI.shortener("\n\nLINUX VA: " + "Did you know that, " + x)
        speak("Did you know that, " + x)

    elif "weather" in text or "temperature" in text:
        print("The temperature today in Hyderabad is " + str(temp()) + " degree celsius with " + str(des()))
        GUI.shortener("\n\nLINUX VA: The temperature today in Hyderabad is " + str(temp()) + " degree celsius with " + str(des()))
        speak("The temperature today in Hyderabad is " + str(temp()) + " degree celsius with " + str(des()))

    elif "today" and "date" in text:
        x = "\n\nLINUX VA: Today is " + today_date.strftime("%d") + " of" + today_date.strftime("%B") + " And its currently " + (
            today_date.strftime("%I")) + " " + (today_date.strftime("%M")) + (today_date.strftime("%p"))
        GUI.shortener(x)
        speak("Today is " + today_date.strftime("%d") + " of" + today_date.strftime("%B") + " And its currently " + (
            today_date.strftime("%I")) + " " + (today_date.strftime("%M")) + (today_date.strftime("%p")))

    elif "sublime" in text:
        GUI.shortener("\n\nLINUX VA: Opening Sublime Text")
        speak("Opening Sublime Text")
        os.system("/snap/sublime-text/current/opt/sublime_text/sublime_text")
        time.sleep(5)

    elif "open" and "chrome" in text:
        GUI.shortener("\n\nLINUX VA: Opening Chrome")
        speak("Opening Chrome")
        assist = selenium_web.infow()
        time.sleep(3)

    elif "run" and "command" in text:
        subprocess.run(["python3", "weather.py"])

    elif "exit" in text:
        GUI.shortener("\n\nLINUX VA: Okay Bye! Take Care")
        speak("Okay Bye! Take Care")
        quit()

    elif "hello" in text:
            GUI.shortener("\n\nLINUX VA: Hi! How can I help you?")
            speak("Hi! How can I help you?")

    elif "hi" in text or "hai" in text:
            GUI.shortener("\n\nLINUX VA: Hello! How can I help you?")
            speak("Hello! How can I help you?")

    else:
        GUI.shortener("\n\nLINUX VA: Could not understand you. Can you please repeat?")
        speak("Could not understand you. Can you please repeat?")
