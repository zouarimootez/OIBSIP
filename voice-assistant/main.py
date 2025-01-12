from core.speech_recognition import listen_to_user
from core.text_to_speech import speak
from core.nlp_processor import process_input
from core.task_executor import execute_task
from utils.logger import log

def main():
    speak("Hello, how can I help you?")
    while True:
        user_input = listen_to_user()
        if user_input:
            if "exit" in user_input.lower():
                speak("Goodbye!")
                break
            intent = process_input(user_input)
            response = execute_task(intent)
            speak(response)
            log(f"User: {user_input} | Assistant: {response}")

if __name__ == "__main__":
    main()