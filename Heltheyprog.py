
#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from  time import time


def musiciconloop(file, stoper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_user=input()
        if input_user== stoper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylog.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    # musiciconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersec=5
    eyesec=20
    exesec=30
    while True:
        if time() - init_water > watersec:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiciconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyesec:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiciconloop('water.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exesec:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiciconloop('water.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")

