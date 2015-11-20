'''
Created on 19.11.2015

@author: romanborn
'''

from controller.classController import Controller

from RPi import GPIO #@UnresolvedImport

if __name__ == '__main__':
    try:
        controller = Controller('params.ini')
        controller.run()
        
        GPIO.cleanup()
    
    except (KeyboardInterrupt):
        print("keyboard interrupt")
        GPIO.cleanup()
    
    '''    
    except:
        GPIO.cleanup()
    '''
    