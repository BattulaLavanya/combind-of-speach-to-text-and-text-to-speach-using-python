# Python program to translate speech to text and text to speech

import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
import pygame, time
from datetime import datetime


def SpeakText(command):
    language = 'en'
    myobj = gTTS(text=command, lang=language, slow=False)
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    myobj.save(filename)
    pygame.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(2)
    pygame.mixer.music.fadeout(2)
    
    
    
r = sr.Recognizer()
print("Say Something")

d=1
while (d):                                                      
    try:                                                      
        with sr.Microphone() as source2:                       
            r.adjust_for_ambient_noise(source2, duration=0.2)  
            audio2 = r.listen(source2,phrase_time_limit =8)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            if MyText=='bye':
                d=0
            print("You said "+MyText)
            SpeakText(MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")

