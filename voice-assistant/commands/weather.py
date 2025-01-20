import requests
from speech import text_to_speech
def get_weather(city):
    api_key = "your api key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        description = weather["description"]
        text_to_speech.speak(f"The temperature in {city} is {temperature} degrees Celsius with {description}.")
    else:
        text_to_speech.speak("City not found. Please try again.")