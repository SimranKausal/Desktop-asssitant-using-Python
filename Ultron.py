import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
import pywhatkit 
import smtplib


from Intro import play_gif 
play_gif
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18: 
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am Jarvis Mam. Please tell me how may I help you.") 

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        r.pause_threshold = 1
        r.energy_threshold = 600
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") 
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query.lower() 


def search_wikipedia(query):
    if 'wikipedia' in query: 
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("jarvis", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

def date():
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    current_date = datetime.datetime.now().day
    speak("The current date is:")
    speak(current_date)
    speak(current_month)
    speak(current_year)
    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kaushalsimran620@gmail.com', 'Simran@25')
    server.sendmail('kaushalsimran620@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()
        search_wikipedia(query)

        if "hello" in query:
            speak("Hello mam, how are you?")
        elif "i am fine" in query:
            speak("That's great, mam")   
        elif "how are you" in query:
            speak("Perfect, mam")
        elif "thank you" in query:
            speak("You are welcome,Mam" )
        elif "google" in query:
             from SearchNow import searchGoogle
             searchGoogle(query)
        # elif "youtube"in query:
        #  from SearchNow import searchYoutube
        #  searchYoutube(query)
        # elif "wikipedia" in query:
        #    from SearchNow import searchWikipedia
        #    searchWikipedia(query)
        elif "open youtube" in query:
            speak("Opening Youtube, Mam")
            webbrowser.open("https://www.youtube.com") 
        # elif "open google" in query:
        #     speak("Opening Google, Mam")
        #     webbrowser.open("https://www.google.com")
        # elif "google" in query:
        #    speak("What do you want to search on Google, Mam?")
        #    search_query = take_command().lower()
        #    speak("this is what i found on google mam")
        #    search_url = "https://www.google.com/search?q="
        #    webbrowser.open(search_url + search_query)
        
        elif "open instagram" in query:
            speak("Opening Instagram, Mam") 
            webbrowser.open("https://www.instagram.com")
        elif "open wikipedia" in query:
            speak('Opening Wikipedia, Mam')
            webbrowser.open("https://www.wikipedia.com")
        elif "open spotify" in query:
            speak('Opening Spotify, Mam')
            webbrowser.open("https://open.spotify.com/")
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")
        elif "open code" in query:
            codepath = "C:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('Opening Code, Mam')
            os.startfile(codepath)
        elif "temperature" in query or "weather" in query:
            search = "temperature in Delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {search} is {temp}")
        elif "exit" in query or "bye" in query:
            speak("Goodbye, Mam")
            break
        elif "Email to Simran" in query:

            try:
                speak("What should I speak?")
                content = take_command()
                to = "kaushalsimran620@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this Email at the moment")
            
        elif"date"in query:

           date()

        elif "click my photo" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            pyttsx3.speak("SMILE")
            pyautogui.press("enter")
           
        elif "screenshot" in query:
            im = pyautogui.screenshot()
            im.save("ss.jpg")
            
        elif "remember that" in query:
            rememberMessage = query.replace("remember that", "")
            rememberMessage = query.replace("jarvis", "")
            pyttsx3.speak("You told me to remember that" + rememberMessage)
            remember = open("Remember.txt", "a")
            remember.write(rememberMessage)
            remember.close()
              
            

        