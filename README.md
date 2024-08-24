# CodexCue Python Development Internship Projects

This repository contains projects developed during the CodexCue Python Development Internship program. The projects cover various Python applications, including URL shortening, a Pygame music player, a plagiarism checker, and a voice assistant.

## Table of Contents

1. [URL Shortener](#url-shortener)
2. [Pygame Music Player](#pygame-music-player)
3. [Plagiarism Checker](#plagiarism-checker)
4. [Voice Assistant](#voice-assistant)
5. [Installation](#installation)
6. [License](#license)

## URL Shortener

A simple URL shortener built using Python. This application generates a short URL corresponding to a long URL and allows retrieval of the original URL using the short version.

### Features

- Generate short URLs.
- Retrieve the original URL using the short URL.
- Open the URL directly in a web browser.

### Usage

1. Run the script `url_shortener.py`.
2. Enter the URL to shorten.
3. Retrieve the original URL using the generated short URL.

## Pygame Music Player

A music player application using Python's `pygame` library. It allows users to play `.mp3` and `.wav` files, with controls to pause, resume, stop, and change songs.

### Features

- List available music files from a specified directory.
- Select and play songs.
- Control playback (pause, resume, stop, change song).

### Usage

1. Ensure your music files are located in the specified directory (default is `H:\music`).
2. Run the script `music_player.py`.
3. Follow the on-screen instructions to select and control music playback.

## Plagiarism Checker

A tool to detect plagiarism by comparing text documents for similarities. It uses the Natural Language Toolkit (NLTK) for natural language processing.

### Features

- Load and compare two text documents.
- Identify the percentage of similarity between the two texts.
- Exclude common stopwords from the comparison.

### Usage

1. Run the script `plagiarism_checker.py`.
2. Load two text files to compare.
3. The similarity percentage will be displayed on the screen.

## Voice Assistant

A voice-controlled personal assistant developed using Python. It leverages speech recognition libraries like `SpeechRecognition` and text-to-speech libraries like `pyttsx3`.

### Features

- Voice-controlled interaction.
- Tells the current time.
- Opens Google and performs other tasks based on voice commands.

### Usage

1. Run the script `voice_assistant.py`.
2. Use voice commands to interact with the assistant.

## Installation

### Prerequisites

- Python 3.x
- Required Python libraries:
  - `pygame`
  - `speech_recognition`
  - `pyttsx3`
  - `nltk`
  - `tkinter`

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
   cd your-repository-name
   ```
2. Install the required libraries:

```bash
pip install pygame speechrecognition pyttsx3 nltk
```
Run the desired project script as mentioned in each project's usage section.
