# Pygame Music Player

This project is a simple command-line music player built using Python and the `pygame` library. It allows users to play, pause, resume, stop, and change songs from a specified directory containing `.mp3` and `.wav` files.

## Features

- **Play Music**: Load and play selected songs from the directory.
- **Pause and Resume**: Control playback with pause and resume functionalities.
- **Stop Playback**: Stop the current song and halt playback.
- **Change Song**: Switch to a different song while playing.
- **Command-Line Interface**: Simple text-based interface for user commands.

## Requirements

- Python 3.x
- `pygame` library

You can install the `pygame` library using pip:

```bash
pip install pygame
```
## Usage
1: Run the Script: Execute the script to start the music player:

```bash
python music_player.py
```

2: Enter Directory Path: Provide the directory path where your music files are located when prompted.

3: Available Commands:

p: Pause the current song.
r: Resume the paused song.
s: Stop the current song.
c: Change the song. You will be prompted to select a new song from the list.
q: Quit the music player.


4: Song Selection: After starting the player, you will see a list of available songs. Enter the number corresponding to the song you want to play.

## Code Overview
Directory Path Input: The script asks for the directory path containing music files and validates its existence.

List Songs: The script scans the directory for .mp3 and .wav files and displays them.

Play Song: Load and play the selected song using pygame.mixer.

Handle Commands: Provides functionalities to control playback and change songs based on user commands
