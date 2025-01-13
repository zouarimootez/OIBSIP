import requests
from speech.text_to_speech import speak

def get_news():
    api_key = "your api key"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "ok":
        articles = data["articles"][:5]
        for article in articles:
            speak(article["title"])
    else:
        speak("Sorry, I couldn't fetch the news.")