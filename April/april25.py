# Healthy programmer Reminder

'''
    9am - 5pm

    water - water.mp3 (3.5 l) - drank - log - every 40 min
    Eyes - eyes.mp3 - every 30 mins - eydone
    physical activity - physical.mp3 - every 45min -exdone


   --> rules:

    1> pygame module to play audio
'''

from pygame import mixer
from datetime import datetime
from time import time

def music_loop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
     
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_file(msg):
    with open("April\mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()} \n")

if __name__ == '__main__':
    # music_loop(".\cource\water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 2
    eyessec = 1800
    exsecs = 2700

    while True:
        if time()-init_water > watersecs:
            print("water drinking time.Enter the 'drank' to stop the alarm.")
            music_loop("cource\water.mp3", 'drank')
            init_water = time()
            log_file("drank water at ")

        if time()-init_eyes > eyessec:
            print("Eyes exercise time.Enter the 'eydone' to stop the alarm.")
            music_loop("cource\water.mp3", 'eydone')
            init_eyes = time()
            log_file("Done Eyes-Exercise at ")

        if time()-init_exercise > exsecs:
            print("physical exercise time.Enter the 'exdone' to stop the alarm.")
            music_loop("cource\water.mp3", 'exdone')
            init_exercise = time()
            log_file("Done Physical-Exercise at ")
