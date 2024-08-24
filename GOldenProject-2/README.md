# Voice Assistant

This Python-based Voice Assistant allows users to interact through voice commands. It utilizes speech recognition to understand spoken words and text-to-speech to provide vocal responses. The assistant can perform basic tasks like telling the time and opening a web browser.

## Features

- **Voice Interaction**: Recognizes spoken commands using Google's Web Speech API.
- **Text-to-Speech Response**: Responds to commands using `pyttsx3`.
- **Command Handling**:
  - **Greeting**: Responds to "Hello" or "Hey".
  - **Time Inquiry**: Tells the current time.
  - **Web Browsing**: Opens Google in the default browser.
  - **Exit**: Stops the assistant with a "Quit" command.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `pyaudio`

### Install the dependencies:

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```
### Running the Assistant
Execute the script to start the voice assistant:

```bash
python voice_assistant.py
```

## Using the Assistant

- **Greetings**: Say "Hello" or "Hey" to initiate a response.
- **Time Check**: Ask, "What is the time?" to hear the current time.
- **Open Google**: Say "Open Google" to launch Google in your browser.
- **Exit**: Say "Quit" to stop the assistant.

## How It Works

### Speech Recognition:

- Uses `speech_recognition` to capture audio and convert it into text.
- Relies on Google’s Web Speech API for accurate transcription.

### Text-to-Speech:

- Employs `pyttsx3` to convert text responses into speech.
- Allows customization of voice properties like rate, volume, and voice type.

### Command Handling:

- The assistant listens continuously for commands.
- Depending on the recognized command, it performs specific actions like telling the time or opening a website.
