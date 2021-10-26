from typing import cast
from pygame import mixer  # Load the popular external library
import time
import sys
import os
import sys
import psutil
import logging
from pynput import keyboard


def restart_timer():
    print("----------Restarting timer----------")
    restart_program()

def restart_program():
    """Restarts the current program
    """
    os.execl(sys.executable, 'python', __file__, *sys.argv[1:])

keyboard.GlobalHotKeys({'<ctrl>+r': restart_timer}).start()


if __name__ == '__main__': 
    
    farming_period = 0
    loot_period = 0
    try:
        file = open('../properties.txt')
        lines = file.readlines()
        farming_period = int(lines[0].split(':')[1].replace(" ", ""))    
        loot_period = int(lines[1].split(':')[1].replace(" ", ""))    
    except Exception as e:
        print(e)

    
    mixer.init()
    
    try:
        while True:
            time.sleep(farming_period)
            mixer.music.load('../sounds/monney.mp3')
            mixer.music.play() 
            time.sleep(loot_period-3)
            
    except KeyboardInterrupt:
        pass
    
 

