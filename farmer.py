from pygame import mixer  # Load the popular external library
import time
import sys

if __name__ == '__main__': 
    
    farming_period = 90
    loot_period = 30

    if len(sys.argv) == 2:
        farming_period = sys.argv[1]
        loot_period = sys.argv[2] 
    
    mixer.init()
    
    try:
        while True:
            time.sleep(farming_period)
            mixer.music.load('sounds/monney.mp3')
            mixer.music.play() 
            time.sleep(loot_period-3)
            
    except KeyboardInterrupt:
        pass
    
 