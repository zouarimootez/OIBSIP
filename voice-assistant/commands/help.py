from speech.text_to_speech import speak

def help_menu():
    speak("Here are some commands you can try:")
    commands = [
        "Say 'hello' to greet me.",
        "Say 'wikipedia' followed by a topic to search Wikipedia.",
        "Say 'search' followed by a query to search the web.",
        "Say 'open YouTube' or 'open Google' to open websites.",
        "Say 'play music' to open Spotify.",
        "Say 'time' or 'date' to get the current time or date.",
        "Say 'weather' to get the weather for a city.",
        "Say 'set reminder' to set a reminder.",
        "Say 'send email' to send an email.",
        "Say 'tell me a joke' to hear a joke.",
        "Say 'news' to get the latest news.",
        "Say 'exit' to close the program."
    ]
    for cmd in commands:
        speak(cmd)