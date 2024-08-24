import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Ask the user for the music directory
music_dir = input("Enter the directory path where your music files are located: ")

# Check if the directory exists
if not os.path.exists(music_dir):
    print("The specified directory does not exist. Please check the path and try again.")
    exit()

# Get a list of all .mp3 and .wav files in the specified directory
songs = [song for song in os.listdir(music_dir) if song.endswith('.mp3') or song.endswith('.wav')]

# Function to play a selected song
def play_song(song):
    pygame.mixer.music.load(os.path.join(music_dir, song))
    pygame.mixer.music.play()

# Display the list of available songs
def show_songs():
    print("Available songs:")
    for index, song in enumerate(songs):
        print(f"{index + 1}. {song}")

# Function to handle user commands
def handle_commands():
    while True:
        command = input("\nEnter command (p: pause, r: resume, s: stop, c: change song, q: quit): ").lower()

        if command == 'p':
            pygame.mixer.music.pause()
        elif command == 'r':
            pygame.mixer.music.unpause()
        elif command == 's':
            pygame.mixer.music.stop()
        elif command == 'c':
            show_songs()
            song_choice = int(input("Enter the song number to play: ")) - 1
            if 0 <= song_choice < len(songs):
                play_song(songs[song_choice])
            else:
                print("Invalid song choice!")
        elif command == 'q':
            pygame.mixer.music.stop()
            print("Quitting music player.")
            break
        else:
            print("Invalid command! Please try again.")

# Main function to start the music player
def main():
    if not songs:
        print("No songs found in the specified directory.")
        return

    print("Welcome to the Pygame Music Player!")
    show_songs()

    song_choice = int(input("Enter the song number to play: ")) - 1
    if 0 <= song_choice < len(songs):
        play_song(songs[song_choice])
        handle_commands()
    else:
        print("Invalid song choice!")

if __name__ == "__main__":
    main()
