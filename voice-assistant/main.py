import webbrowser

import wikipedia
from speech.text_to_speech import speak
from speech.speech_recognition import listen
from commands.help import help_menu
from commands.web_search import search_web
from commands.weather import get_weather
from commands.reminders import set_reminder
from commands.email import send_email
from commands.jokes import tell_joke
from commands.news import get_news
from utils.datetime_utils import greet
import datetime

def execute_command(command):
    if "hello" in command:
        speak("Hello there!")
    elif 'wikipedia' in command:
        speak('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak('According to Wikipedia')
        print(results)
        speak(results)
    elif "search" in command:
        search_query = command.split("search")[-1].strip()
        search_web(search_query)
    elif 'open youtube' in command:
        webbrowser.open("youtube.com")
    elif 'open google' in command:
        webbrowser.open("google.com")
    elif 'play music' in command:
        webbrowser.open("spotify.com")
    elif 'time' in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")
    elif 'date' in command:
        now = datetime.datetime.now().strftime("%D-%m-%Y")
        speak(f"The date is {now}")
    elif "weather" in command:
        speak("Which city's weather would you like to know?")
        city = listen().lower()
        if city:
            get_weather(city)
    elif "set reminder" in command:
        set_reminder()
    elif "send email" in command:
        speak("Who should I send the email to?")
        to = listen().lower()
        if to:
            speak("What is the subject?")
            subject = listen().lower()
            if subject:
                speak("What should I say in the email?")
                body = listen().lower()
                if body:
                    send_email(to, subject, body)
    elif "tell me a joke" in command:
        tell_joke()
    elif "news" in command:
        speak("Fetching the latest news...")
        get_news()
    elif "help" in command:
        help_menu()
    elif 'exit' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I couldn't understand your command.")

if __name__ == "__main__":
    greet()
    while True:
        command = listen().lower()
        if command:
            execute_command(command)