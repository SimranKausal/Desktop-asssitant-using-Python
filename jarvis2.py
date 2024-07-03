import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def WishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am Jarvis Ma'am. Please tell me how may I help you") 

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    WishMe()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening YouTube Ma'am")
            webbrowser.open("https://www.youtube.com") 

        elif 'open google' in query:
            speak("Opening Google Ma'am")
            webbrowser.open("https://www.google.com")
        
        elif 'open instagram' in query:
            speak("Opening Instagram Ma'am")
            webbrowser.open("https://www.instagram.com")

        elif 'open wikipedia' in query:
            speak("opening wikipedia mam")
            webbrowser.open("https://www.wikipedia.org")
 
        elif 'open spotify' in query:
            speak("Opening Spotify Mam")
            webbrowser.open("https://open.spotify.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, the time is {strTime}")

        elif 'open code' in query:
            speak("opening code mam")
            codepath = "C:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
