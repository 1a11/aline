import speech_recognition as sr  
import os
import pyttsx3

class recog():
    def __init__(self):
        words = list()
    def talk(self, word):
        engine = pyttsx3.init()
        engine.say(word)
        engine.runAndWait()
        print(word)
        
    def repeat(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Скажите что-нибудь')
            r.pause_treshold = 1
            r.adjust_for_ambient_noise(source,1)
            audio = r.listen(source)
        try:
            zadanie = r.recognize_google(audio, language = "ru-RU").lower()
            talk('Вы сказали '+zadanie)
            words.append(zadanie)
            #talk(' '+ zadanie.replace('',''))
        except sr.UnknownValueError:
            talk('Я вас не понимаю')
            zadanie = repeat()
        return zadanie
        
