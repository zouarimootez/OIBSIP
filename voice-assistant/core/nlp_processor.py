# import openai
# from utils.config import OPENAI_API_KEY

# openai.api_key = OPENAI_API_KEY

# def process_input(user_input):
#     # Use the ChatCompletion API with the gpt-3.5-turbo model
#     response = openai.ChatCompletion.create(
#         model="gpt2",  # Use the newer model
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": user_input}
#         ],
#         max_tokens=50  # Limit the response length
#     )
#     # Extract and return the assistant's reply
#     return response.choices[0].message['content'].strip()


# import openai
# from utils.config import OPENAI_API_KEY

# # Set the OpenAI API key
# openai.api_key = OPENAI_API_KEY

# # Define the prompt to be sent
# prompt = 'Please generate a simple blog post according to this title "What is CHATGPT"'

# # Define the default model if none is specified
# default_model = 'gpt-3.5-turbo'

# # Uncomment the model you want to use, and comment out the others
# # model = 'gpt-4'
# # model = 'gpt-4-32k'
# # model = 'gpt-3.5-turbo-0125'
# model = default_model

# def process_input(user_input):
#     # Use the ChatCompletion API with the specified model
#     response = openai.ChatCompletion.create(
#         model=model,  # Use the specified model
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": user_input}
#         ],
#         max_tokens=500  # Adjust the response length as needed
#     )
#     # Extract and return the assistant's reply
#     return response.choices[0].message['content'].strip()

# try:
#     # Process the prompt and get the response
#     blog_post = process_input(prompt)
#     print(blog_post)

# except Exception as e:
#     # Print any errors
#     print(f'Error: {e}')




def classify_intent(text):
    text = text.lower()
    if "weather" in text:
        return "WeatherQuery"
    elif "music" in text or "play" in text:
        return "PlayMusic"
    elif "alarm" in text or "set" in text:
        return "SetAlarm"
    else:
        return "UnknownIntent"

# Test
texts = [
    "What is the weather like today?",
    "Play some music for me.",
    "Set an alarm for 7 AM.",
]

for text in texts:
    intent = classify_intent(text)
    print(f"Input: {text}\nPredicted Intent: {intent}\n")