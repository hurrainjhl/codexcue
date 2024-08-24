import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    print(f"Speaking: {text}")  # Debugging statement
    engine.say(text)
    engine.runAndWait()

# Function to take voice input from the user
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")  # Debugging statement
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, I'm unable to connect to the service.")  # Debugging statement
            speak("Sorry, I'm unable to connect to the service.")
            return ""

# Function to handle commands
def handle_command(command):
    print(f"Handling command: {command}")  # Debugging statement

    if any(word in command for word in ['hello', 'hey']):
        speak("Hello! How can I assist you today?")
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif 'open google' in command:
        webbrowser.open('https://www.google.com')
        speak("Opening Google")
    elif 'quit' in command:
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I didn't get that.")
    return True

# Main loop to run the assistant
def start_assistant():
    speak("Voice Assistant activated.")
    while True:
        command = listen()
        if not handle_command(command):
            break

# Set properties before adding anything to speak
def configure_engine():
    engine.setProperty('rate', 150)    # Speed percent (default: 200)
    engine.setProperty('volume', 0.9)  # Volume 0-1 (default: 1)

    # Set a specific voice (if available)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change index based on your available voices

# Call configure_engine() before starting the assistant
configure_engine()


# Start the voice assistant
if __name__ == "__main__":
    start_assistant()
