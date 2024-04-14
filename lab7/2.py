import pygame
import os

# Initialize Pygame mixer
pygame.mixer.init()

# Set up the keyboard controls
KEY_PLAY = pygame.K_SPACE
KEY_STOP = pygame.K_s
KEY_NEXT = pygame.K_RIGHT
KEY_PREVIOUS = pygame.K_LEFT

# Set the directory containing your music files
MUSIC_DIRECTORY = 'C:\\Users\\Nurlan\\Desktop\\PP2_2024\\Lab7\\musics'

# Get a list of all music files in the directory
music_files = [os.path.join(MUSIC_DIRECTORY, f) for f in os.listdir(MUSIC_DIRECTORY) if f.endswith('.mp3') or f.endswith('.wav')]

# Initialize Pygame
pygame.init()

# Set up the display (we don't need a display for this player)
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

# Variables to keep track of the current song and pause position
current_song_index = 0
is_playing = False
pause_position = 0

# Load the first song
if music_files:
    pygame.mixer.music.load(music_files[current_song_index])

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Play/pause the current song
            if event.key == KEY_PLAY:
                if is_playing:
                    pygame.mixer.music.pause()
                    pause_position = pygame.mixer.music.get_pos()
                else:
                    pygame.mixer.music.unpause()
                    if pause_position > 0:
                        pygame.mixer.music.play(0, pause_position / 1000.0)
                is_playing = not is_playing
            # Stop the current song
            elif event.key == KEY_STOP:
                pygame.mixer.music.stop()
                is_playing = False
                pause_position = 0
            # Play the next song
            elif event.key == KEY_NEXT:
                current_song_index = (current_song_index + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_song_index])
                pygame.mixer.music.play()
                is_playing = True
                pause_position = 0
            # Play the previous song
            elif event.key == KEY_PREVIOUS:
                current_song_index = (current_song_index - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_song_index])
                pygame.mixer.music.play()
                is_playing = True
                pause_position = 0

    # Update the display (not used in this case)
    pygame.display.flip()

# Quit Pygame
pygame.quit()