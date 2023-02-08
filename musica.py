import time
import pygame

def schedule_music_play(music_file, play_time):
    # Calculate the number of seconds until the play time
    play_time_seconds = time.mktime(time.strptime(play_time, '%Y-%m-%d %H:%M:%S'))
    wait_time_seconds = play_time_seconds - time.time()
    
    if wait_time_seconds < 0:
        print("Play time is in the past, cannot schedule music play")
        return
    
    # Wait until the play time
    time.sleep(wait_time_seconds)
    
    # Initialize the pygame mixer
    pygame.mixer.init()
    
    # Load the music file
    pygame.mixer.music.load(music_file)
    
    # Play the music
    pygame.mixer.music.play()
    
    # Wait until the music finishes playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)


# Schedule a music play for the current time
schedule_music_play("musica.mp3.mp3", time.strftime("2023-02-07 04:07:00"))

