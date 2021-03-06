from pygame import mixer  # Load the popular external library
import time
import sys

if __name__ == '__main__': 
    

    file = open('../properties.txt')
    lines = file.readlines()
    farming_period = int(lines[0].split(':')[1].replace(" ", ""))    
    loot_period = int(lines[1].split(':')[1].replace(" ", ""))    


    if len(sys.argv) == 2:
        farming_period = sys.argv[1]
        loot_period = sys.argv[2] 
    
    mixer.init()
    
    try:
        while True:
            time.sleep(farming_period)
            mixer.music.load('../sounds/monney.mp3')
            mixer.music.play() 
            time.sleep(loot_period-3)
            
    except KeyboardInterrupt:
        pass
    
 