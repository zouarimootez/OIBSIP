import time
from speech.text_to_speech import speak
from speech.speech_recognition import listen

def set_reminder():
    speak("What should I remind you about?")
    reminder = listen().lower()
    if reminder:
        speak("In how many minutes?")
        try:
            minutes = int(listen().lower())
            time.sleep(minutes * 60)
            speak(f"Reminder: {reminder}")
        except ValueError:
            speak("Sorry, I didn't understand the time.")