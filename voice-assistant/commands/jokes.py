import pyjokes
from speech.text_to_speech import speak

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)