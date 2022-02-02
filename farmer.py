from typing import cast
from pygame import mixer  # Load the popular external library
import time
import sys
import os
import psutil
import logging
from pynput import keyboard


if os.name == 'nt':
    import msvcrt
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def remove_curser():
    hide_cursor()

def clear_line():
    print(f"                                 ", end="\r")

def starting_timer():
    print("---------Starting timer---------")


def restart_timer():
    print("----------Restarting timer----------")
    restart_program()
    

def restart_program():
    """Restarts the current program
    """
    clearConsole()
    os.execl(sys.executable, 'python', __file__, *sys.argv[1:])


keyboard.GlobalHotKeys({'<ctrl>+r': restart_timer}).start()


if __name__ == '__main__': 
    remove_curser()
    starting_timer()
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
            for tick in range(farming_period):
                time.sleep(1)
                print(f"Farming : {tick+1}", end="\r")
            clear_line() 
            mixer.music.load('../sounds/monney.mp3')
            mixer.music.play() 
            for tick in range(loot_period-3):
                time.sleep(1)
                print(f"looting : {tick+1+3}", end="\r")
            clear_line()
    except KeyboardInterrupt:
        pass
    
 
