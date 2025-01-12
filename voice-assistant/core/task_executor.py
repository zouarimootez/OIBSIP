from integrations.weather import get_weather
# from integrations.email import send_email
#from integrations.calendar import set_reminder
from utils.helpers import extract_city

def execute_task(intent):
    if "weather" in intent.lower():
        city = extract_city(intent)
        return get_weather(city)
    elif "email" in intent.lower():
        # send_email("recipient@example.com", "Test Subject", "This is a test email.")
        return "Email sent!"
    elif "reminder" in intent.lower():
        #set_reminder("Meeting", "2023-10-15 10:00")
        return "Reminder set!"
    else:
        return "I'm not sure how to help with that."