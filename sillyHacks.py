import os
from gtts import gTTS
import speech_recognition as sr
import webbrowser
import requests
from bs4 import BeautifulSoup
from googlesearch import search 
from time import sleep
import imdb
import smtplib
import pykintone


#Kintone
('sillyHacks.json')

#Speech Recognition
#This is global so it can be called in any function
r = sr.Recognizer()

#Reads a text
def Speak(audio):
    tts = gTTS(text = audio, lang = 'en', slow = False)
    tts.save('eva.mp3')                 #Saves the mp3 file
    os.system('start eva.mp3')          #Plays mp3 file

#Listens for commands/responses
def Mic():
    with sr.Microphone() as mic:
        print ("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(mic, duration = 1)
        audio = r.listen(mic)                           #Activates mic
        command = ""

        try:
            command = r.recognize_google(audio)
        
        except Exception as e:
            print("Exception: " + str(e))

        return command.lower()

#Introduction to program
def myIntro():
    Speak("Hi! My name is Ava, I am everybody's virtual assisant."); sleep(4.2)
    
    Speak("What is your name?"); sleep(2.2)

    with sr.Microphone() as mic:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(mic, duration = 1)
        audio = r.listen(mic)                           #Activates mic
        name = ""

        try:
            name = r.recognize_google(audio)
        
        except Exception as e:
            print("Exception: " + str(e))

        Speak("Hi " + str(name) + ", nice to meet you. Please ask me anything, I'll do my best to assist you.")

def myCommands(command):
    if "how" and "girlfriend" in command:
        print("Please smile for the camera")
        Speak("Please smile for the camera"); sleep(3.5)
        print("3, 2, 1")
        Speak("3, 2, 1"); sleep (2.2)
        print("Click")
        Speak("Click"); sleep (1.5)
        print("Processing facial structure")
        Speak("Processing facial structure"); sleep(4.2)
        print("Give me a moment, I am getting a headache")
        Speak("Give me a moment, I am getting a headache"); sleep(7.2)
        print("Results are in: Its hard to say, but this might help")
        Speak("Results are in: Its hard to say, but this might help"); sleep(8.2)
        webbrowser.open('https://www.wikihow.com/Get-a-Girlfriend')

    if "how" and "boyfriend" in command:
        print("Please smile for the camera")
        Speak("Please smile for the camera"); sleep(3.5)
        print("3, 2, 1")
        Speak("3, 2, 1"); sleep (2.2)
        print("Click")
        Speak("Click"); sleep (1.5)
        print("Processing facial structure")
        Speak("Processing facial structure"); sleep(4.2)
        print("Give me a moment, I am getting a headache")
        Speak("Give me a moment, I am getting a headache"); sleep(7.2)
        print("Results are in: Its hard to say, but this might help")
        Speak("Results are in: Its hard to say, but this might help"); sleep(8.2)
        webbrowser.open('https://www.wikihow.com/Get-a-Boyfriend')

    if "play music" in command:
        Speak("Okay I will play a song")        #Future Implementations: Choose a song and what platform you would like to play it on
        webbrowser.open('https://soundcloud.com/nocopyrightsounds/alan-walker-fade-ncs-release')

    if "weather" in command:
        Speak("The current weather is")
        webbrowser.open('https://www.google.com/search?q=what+is+the+weather&rlz=1C1SQJL_enUS862US862&oq=what+is+the+weather&aqs=chrome..69i57j0l7.4120j1j7&sourceid=chrome&ie=UTF-8')

    if "how long" and "finish" in command:
        URL = ""
        showTitle = str(command.split("finish ")[-1]) #Takes the end of the command, which is the title of the show

        query = "how many episodes are in {} imdb".format(showTitle)    #word "imdb" must be in every search for imdbPy to work
  
        for j in search(query, tld="com", num=1, stop=1, pause=2): 
            URL = j
        
        
        code = ""
        data = URL.split("/")
        for i in data:
            if i[0:2] == "tt":
                code = i[2:]
        
        # creating instance of IMDb 
        ia = imdb.IMDb() 
        
        
        # getting information 
        series = ia.get_movie(code) 
        
        # adding new info set 
        ia.update(series, 'episodes') 
        
        # getting episodes of the series 
        episodes = series.data['episodes'] 
        
        # printing the object i.e name 
        print(series) 
        
        # printing total episodes of each season 
        # traversing each key
        total = 0 
        for i in episodes.keys(): 
            
            # getting total episode in season i 
            n = len(episodes[i]) 
            total += n  
            # printing total episodes 
            print("Total Episodes in Season {} : {}".format(i,n)) 
        print("Total Episodes: {}".format(total))

    if "bye" in command:
        quit()

def main():
    power = True
    
    myIntro()
    while power == True:
        myCommands(Mic())

main()