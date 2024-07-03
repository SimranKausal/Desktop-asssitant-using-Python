import pyttsx3
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def set_alarm():
    while True:
        alarm_time = input("Please enter the time for the alarm (in HH:MM format): ")
        try:
            datetime.datetime.strptime(alarm_time, '%H:%M')
            break
        except ValueError:
            print("Invalid time format. Please enter time in HH:MM format.")

    with open("AlarmText.txt", "w") as file:
        file.write(alarm_time)

def ring(alarm_time):
    print("Alarm set for:", alarm_time)
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            speak("Alarm ringing")
            os.startfile("bestringtones.net_jarvis-wake-up-iron-man-ringtone.mp3")
            break
        elif current_time >= alarm_time:
            break

# Check if AlarmText.txt exists and contains a valid alarm time
if os.path.exists("AlarmText.txt"):
    with open("AlarmText.txt", "r") as file:
        alarm_time = file.read().strip()
    ring(alarm_time)
else:
    set_alarm()
