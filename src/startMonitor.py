'''
Created on 19.11.2015

@author: romanborn
'''

from controller.classController import Controller
#REMOVE#from RPi import GPIO #@UnresolvedImport

import traceback
import sys

if __name__ == '__main__':
    try:
        if (len(sys.argv) > 1):
            controller = Controller('params.ini', sys.argv[1])
        else:
            controller = Controller('params.ini')

        controller.run()
        
        #REMOVE#GPIO.cleanup()
    
    except (KeyboardInterrupt):
        #REMOVE#GPIO.cleanup()
        print("keyboard interrupt")
        
    except:
        #REMOVE#GPIO.cleanup()
        print("*** EXCEPTION ***")
        print(traceback.format_exc())
