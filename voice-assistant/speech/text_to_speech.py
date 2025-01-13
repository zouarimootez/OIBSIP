import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change the index to use a different voice if needed

def speak(text):
    engine.say(text)
    engine.runAndWait()