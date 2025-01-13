import speech_recognition as sr

# Initialize the speech recognition engine
r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"You said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return ""
    return query