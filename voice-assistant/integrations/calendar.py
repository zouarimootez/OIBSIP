from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build
from utils.config import GOOGLE_CALENDAR_CREDENTIALS

def set_reminder(event_name, event_time):
    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_CALENDAR_CREDENTIALS,
        scopes=["https://www.googleapis.com/auth/calendar"]
    )
    service = build("calendar", "v3", credentials=credentials)
    
    event = {
        "summary": event_name,
        "start": {
            "dateTime": event_time,
            "timeZone": "UTC",
        },
        "end": {
            "dateTime": (datetime.fromisoformat(event_time) + timedelta(hours=1)).isoformat(),
            "timeZone": "UTC",
        },
    }
    
    try:
        service.events().insert(calendarId="primary", body=event).execute()
        return f"Reminder set for {event_name} at {event_time}."
    except Exception as e:
        return f"Failed to set reminder: {str(e)}"