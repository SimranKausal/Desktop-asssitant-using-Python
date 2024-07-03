import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
                                      

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am Jarvis Mam. Please tell me how may I help you") 
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


    
       
    
def sendEmail(to, content): 


 if __name__ == "__main__":
  while(True):
    WishMe()
    query = takecommand().lower()
    if 'wikipedia' in query: 
        speak('Searching wikipedia...')
        query=query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak("opening youtube Mam")
        webbrowser.open("youtube.com") 

    elif 'open google' in query:
        speak("opening google Mam")
        webbrowser.open("www.google.com")
        
    elif 'open instagram' in query:
        speak("opening instagram Mam")
        webbrowser.open("www.instagram.com")

    elif 'open wikipedia' in query:
        speak('opening wikipedia Mam')
        webbrowser.open("wikipedia.com")
 
    elif 'open spotify' in query:
        speak('opening spotify Mam')
        webbrowser.open("https://open.spotify.com/")
 
    elif'the time'in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Mam,the time is{strTime}")
   
 
    elif 'open code' in query:
        codepath = "C:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

   
    
    
    
            


