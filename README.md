---

# BMI Calculator

A simple desktop application to calculate Body Mass Index (BMI) and track BMI history. Built with Python and Tkinter for the GUI, SQLite for data storage, and Matplotlib for data visualization.

---

## Features

- **Calculate BMI**: Enter your weight and height to calculate your BMI and get a health category.
- **BMI History**: View your BMI calculation history in a table.
- **Trend Analysis**: Visualize your BMI trend over time using a line chart.
- **Export Data**: Export your BMI history to a CSV file.

---

## Requirements

- Python 3.x
- Libraries:
  - `tkinter` (included with Python)
  - `sqlite3` (included with Python)
  - `matplotlib` (for plotting BMI trends)
  - `csv` (included with Python)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/zouarimootez/OIBSIP.git
   cd bmi-calculator
   ```

2. **Install dependencies**:
   Install the required libraries using `pip`:
   ```bash
   pip install matplotlib
   ```

3. **Run the application**:
   Navigate to the project directory and run `main.py`:
   ```bash
   python main.py
   ```

---

## Project Structure

```
bmi_calculator/
│
├── __init__.py
├── main.py
│
├── database/
│   ├── __init__.py
│   └── database_manager.py
│
├── gui/
│   ├── __init__.py
│   └── bmi_calculator_gui.py
│
└── utils/
    ├── __init__.py
    └── bmi_utils.py
```

- **`main.py`**: The entry point of the application.
- **`database/`**: Contains the `DatabaseManager` class for handling SQLite database operations.
- **`gui/`**: Contains the `BMI_Calculator_GUI` class for the Tkinter-based user interface.
- **`utils/`**: Contains utility functions for BMI classification and recommendations.

---

## Usage

1. **Calculate BMI**:
   - Enter your weight (in kg) and height (in meters) in the input fields.
   - Click "Calculate BMI" to see your BMI, category, and health recommendation.

2. **View History**:
   - Click "View History" to see a table of all your previous BMI calculations.

3. **Analyze BMI Trend**:
   - In the history window, click "Analyze BMI Trend" to visualize your BMI trend over time.

4. **Export Data**:
   - Click "Export Data" to save your BMI history as a CSV file.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---

## Acknowledgments

- Built with Python and Tkinter.
- Uses SQLite for lightweight database management.
- Matplotlib for data visualization.

---

Enjoy using the BMI Calculator! For any questions or issues, please open an issue on GitHub.


# Password Generator

A secure and customizable password generator application built with Python and Tkinter. This application allows users to generate strong, unique passwords, save them to a local database, and manage user preferences such as themes and fonts.

---

## Features

- **Password Generation**:
  - Generate passwords with customizable length and character sets (uppercase, lowercase, digits, symbols).
  - Option to include a custom character set.
  - Ensures generated passwords are unique and not previously saved in the database.

- **Password Management**:
  - Save generated passwords to a local SQLite database.
  - View password history with timestamps.

- **User Preferences**:
  - Light and dark themes.
  - Customizable font.
  - Save and load user preferences (e.g., default password length, character sets).

- **Password Strength Indicator**:
  - Displays the strength of the generated password (Weak, Medium, Strong).

- **Clipboard Integration**:
  - Copy generated passwords to the clipboard with a single click.

---

## Installation

### Prerequisites

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- `pyperclip` library (for clipboard functionality)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/zouarimootez/OIBSIP.git
   cd password-generator
   ```

2. **Install dependencies**:
   ```bash
   pip install pyperclip
   ```

3. **Run the application**:
   ```bash
   python -m password_generator.main
   ```

---

## Project Structure

```
password_generator/
├── __init__.py
├── main.py
├── gui/
│   ├── __init__.py
│   ├── password_generator_gui.py
│   └── theme_manager.py
├── database/
│   ├── __init__.py
│   └── db_manager.py
├── utils/
│   ├── __init__.py
│   ├── password_utils.py
│   └── preferences_manager.py
└── tests/
    ├── __init__.py
    └── test_password_utils.py
```

---

## Usage

1. **Launch the Application**:
   - Run `python -m password_generator.main` to start the application.

2. **Generate a Password**:
   - Set the desired password length.
   - Choose the character sets (uppercase, lowercase, digits, symbols).
   - Optionally, specify a custom character set.
   - Click "Generate Password" to create a new password.

3. **Save or Copy Password**:
   - Click "Copy to Clipboard" to copy the password.
   - Click "Save Password" to store it in the database.

4. **View Password History**:
   - Click "View Password History" to see previously saved passwords.

5. **Customize Preferences**:
   - Go to the "Settings" menu to change the theme, font, or save preferences.

---

## Testing

To run the unit tests, navigate to the project directory and execute:

```bash
python -m unittest discover password_generator/tests
```

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---

## Acknowledgments

- Built with Python and Tkinter.
- Uses `pyperclip` for clipboard functionality.
- Inspired by the need for secure and customizable password generation.

---

# Voice Assistant

A Python-based voice assistant that can perform various tasks such as web searches, weather updates, setting reminders, sending emails, telling jokes, fetching news, and more. Built with modularity and extensibility in mind, this project uses a **package-oriented architecture** for better organization and maintainability.

---

## Features

- **Speech Recognition**: Listen to user commands using the microphone.
- **Text-to-Speech**: Respond to the user with synthesized speech.
- **Web Search**: Search the web using Google.
- **Weather Updates**: Get the current weather for any city.
- **Reminders**: Set reminders for specific tasks.
- **Email**: Send emails using Gmail's SMTP server.
- **Jokes**: Tell random jokes to lighten the mood.
- **News**: Fetch and read the latest news headlines.
- **Help Menu**: List all available commands.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7 or higher
- Required Python packages (listed in `requirements.txt`)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zouarimootez/OIBSIP.git
   cd voice-assistant
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables (optional):
   - For email functionality, update the `sender_email` and `sender_password` in `voice_assistant/commands/email.py`.
   - For weather and news APIs, replace the API keys in `voice_assistant/commands/weather.py` and `voice_assistant/commands/news.py` with your own keys.

---

## Usage

To start the voice assistant, run the following command:

```bash
python -m voice_assistant.main
```

### Example Commands

- **Greet the assistant**:
  ```
  Hello
  ```
  Response: "Hello there!"

- **Search the web**:
  ```
  Search for Python programming
  ```
  Response: Opens a browser with Google search results for "Python programming".

- **Get the weather**:
  ```
  What's the weather in New York?
  ```
  Response: Provides the current weather in New York.

- **Set a reminder**:
  ```
  Set a reminder
  ```
  Follow the prompts to set a reminder.

- **Send an email**:
  ```
  Send email
  ```
  Follow the prompts to send an email.

- **Tell a joke**:
  ```
  Tell me a joke
  ```
  Response: Tells a random joke.

- **Fetch news**:
  ```
  News
  ```
  Response: Reads the latest news headlines.

- **Exit the program**:
  ```
  Exit
  ```
  Response: "Goodbye!" and the program terminates.

---

## Project Structure

```
voice_assistant/
│
├── voice_assistant/                # Main package
│   ├── __init__.py
│   ├── main.py                     # Entry point for the application
│   ├── speech/                     # Speech-related functionality
│   │   ├── __init__.py
│   │   ├── speech_recognition.py
│   │   ├── text_to_speech.py
│   ├── commands/                   # Command execution logic
│   │   ├── __init__.py
│   │   ├── web_search.py
│   │   ├── weather.py
│   │   ├── reminders.py
│   │   ├── email.py
│   │   ├── jokes.py
│   │   ├── news.py
│   │   ├── help.py
│   ├── utils/                      # Utility functions
│   │   ├── __init__.py
│   │   ├── datetime_utils.py
│   │   ├── api_utils.py
│
├── requirements.txt                # List of dependencies
├── README.md                       # Project documentation
```

---

## Dependencies

The project relies on the following Python packages:

- `speechrecognition`: For speech-to-text conversion.
- `pyttsx3`: For text-to-speech synthesis.
- `wikipedia`: For fetching Wikipedia summaries.
- `requests`: For making HTTP requests to APIs.
- `pyjokes`: For fetching random jokes.
- `smtplib`: For sending emails.

You can install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions are welcome! If you'd like to add new features, fix bugs, or improve the documentation, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---

## Acknowledgments

- Thanks to the developers of the Python libraries used in this project.
- Inspired by virtual assistants like Siri, Alexa, and Google Assistant.

---

## Contact

For questions or feedback, feel free to reach out:

- **Mootez Zouari**: [zouarimootez@gmail.com]
- **Portfolio**: [(https://portfolio-zouarimootezs-projects.vercel.app/)]

---

Enjoy using your voice assistant! 🚀

