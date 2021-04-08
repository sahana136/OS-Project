import pyttsx3 as p
import googletrans
import english
import hindi

gt = googletrans.Translator()

engine = p.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate' , 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

print("Press 1 for english")
speak("Press 1 for english")
inst = "Press two for Hindi"
inst = gt.translate(inst, dest="hi")
print(inst.text)
speak(inst.text)

language = input("Enter your choice: ")

if(language == '1'):
    english.wish()
    while True:
        english.assistant()
elif(language == '2'):
    hindi.wish()
    while True:
        hindi.assistant()