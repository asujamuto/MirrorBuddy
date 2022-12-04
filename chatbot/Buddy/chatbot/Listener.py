#zainstalować dobrze pythona

import speech_recognition as sr
import pyttsx3

def SpeakText(command):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',"Polish")

    
    engine.say(command)
    engine.runAndWait()

def listener():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)

            MyText = r.recognize_google(audio2, language='pl-PL')
            MyText = MyText.lower()

            print("Did you say " + MyText)
        return MyText
    except:
        return "Umarłem"

