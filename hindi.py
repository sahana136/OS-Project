import time

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
import tkinter as tk
from tkinter import *
import speech_recognition as sr
import GUI

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

def wishme():
    hour = int(today_date.hour)
    if hour>0 and hour<12:
        return ("Morning")
    elif hour>=12 and hour<16:
        return ("Afternoon")
    else:
        return ("Evening")

def translate(text):
    text = gt.translate(text, dest='hi')
    text = text.text
    return text

def translate_eng(text):
    text = gt.translate(text, dest='en')
    text = text.text
    return text

def wish():
    wish_d1 = "Hello!" + "Good" + wishme()
    wish_d2 = "I am Linux. Your personal voice assistant. How can I help you?"
    wish_d1 = translate(wish_d1)
    wish_d2 = translate(wish_d2)
    GUI.shortener("\n\nLINUX VA: " + wish_d1 + wish_d2)
    print(wish_d1)
    speak(wish_d1)
    print(wish_d2)
    speak(wish_d2)

def assistant():
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('Listening...')
        audio = r.listen(source)
        text = r.recognize_google(audio, language='hi')
        GUI.shortener("\n\nUSER: " + text)
        print(text)
        text = translate_eng(text)
        text = text.lower()

    if "information" in text:
        tell = "About what topic do you need information?"
        tell = translate(tell)
        GUI.shortener("\n\nLINUX VA: " + tell)
        print(tell)
        speak(tell)

        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print('Listening...')
            audio = r.listen(source)
            info = r.recognize_google(audio)
            info = translate(info)
            GUI.shortener("\n\nUSER: " + info)
        search = "Searching for " + format(info) + " in Google"
        x = translate(search)
        GUI.shortener("\n\nLINUX VA: " + x)
        print(x)
        speak(x)
        assist = selenium_web.infow()
        assist.get_info(info)
        time.sleep(5)

    elif "play" and "video" in text:
        tell = "What video do you want to play?"
        tell = translate(tell)
        GUI.shortener("\n\nLINUX VA: " + tell)
        print(tell)
        speak(tell)

        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print('Listening...')
            audio = r.listen(source)
            vid_title = r.recognize_google(audio)
            GUI.shortener("\n\nUSER: " + vid_title)
        search = "Playing video on Youtube"
        search = translate(search)
        GUI.shortener("\n\nLINUX VA: " + search)
        print(search)
        speak(search)
        pywhatkit.playonyt(vid_title)
        time.sleep(10)

    elif "joke" in text:
        tell = "Sure! Here's your joke"
        tell = translate(tell)
        GUI.shortener("\n\nLINUX VA: " + tell)
        print(tell)
        speak(tell)
        arr = joke()
        GUI.shortener("\n\nLINUX VA: " + translate(arr[0]))
        print(arr[0])
        speak(arr[0])
        GUI.shortener("\n\nLINUX VA: " + translate(arr[1]))
        print(arr[1])
        speak(arr[1])

    elif "fact" in text or "data" in text:
        tell = "Here's a fact for you!"
        tell = translate(tell)
        GUI.shortener("\n\nLINUX VA: " + tell)
        print(tell)
        speak(tell)
        x = randfacts.getFact()
        print(x)
        fact = "Did you know that, " + x
        fact = translate(fact)
        GUI.shortener("\n\nLINUX VA: " + fact)
        print(fact)
        speak(fact)

    elif "weather" in text or "temperature" in text:
        weather = "The temperature today in Hyderabad is " + str(temp()) + " degree celsius with " + str(des())
        weather = translate(weather)
        GUI.shortener("\n\nLINUX VA: " + weather)
        print(weather)
        speak(weather)

    elif "today" and "date" in text:
        today = "Today is " + today_date.strftime("%d") + " of" + today_date.strftime("%B") + " And its currently " + (today_date.strftime("%I")) + " " + (today_date.strftime("%M")) + (today_date.strftime("%p"))
        today = translate(today)
        GUI.shortener("\n\nLINUX VA: " + today)
        print(today)
        speak(today)

    elif "sublime" in text:
        tell = "I am opening"
        tell = translate(tell)
        GUI.shortener("\n\nLINUX VA: " + tell)
        print(tell)
        speak(tell)
        os.system("/snap/sublime-text/current/opt/sublime_text/sublime_text")

    elif "open" and "chrome" in text:
        tell = "I am opening Chrome"
        tell = translate(tell)
        GUI.shortener("\n\nLINUX VA: " + tell)
        print(tell)
        speak(tell)
        assist = selenium_web.infow()

    elif "run" and "command" in text:
        subprocess.run(["python3", "weather.py"])

    elif "hello" in text:
            tell = "Hi. How can I help you?"
            tell = translate(tell)
            GUI.shortener("\n\nLINUX VA: " + tell)
            speak(tell)

    elif "exit" in text or "bye" in text or "leave" in text:
        tell = "Okay Bye! Take care"
        tell = translate(tell)
        GUI.shortener("\n\nLINUX VA: " + tell)
        print(tell)
        speak(tell)
        quit()

    else:
        tell = "Could not understand you. Can you please repeat again?"
        tell = translate(tell)
        GUI.shortener("\n\nLINUX VA: " + tell)
        speak(tell)