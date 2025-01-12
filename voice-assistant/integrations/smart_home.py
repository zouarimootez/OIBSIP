import requests
from utils.config import IFTTT_KEY

def control_smart_home(device, action):
    url = f"https://maker.ifttt.com/trigger/{device}_{action}/with/key/{IFTTT_KEY}"
    try:
        response = requests.post(url)
        if response.status_code == 200:
            return f"Turned {action} the {device}."
        else:
            return "Failed to control the device."
    except Exception as e:
        return f"Error: {str(e)}"