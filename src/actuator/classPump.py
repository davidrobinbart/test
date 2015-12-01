'''
Created on 19.11.2015

@author: romanborn
'''

#REMOVE#from RPi import GPIO #@UnresolvedImport

class Pump:

    def __init__(self, port, description = ''):
        self.GPIOport = port
        self.description = description
        
        #REMOVE#GPIO.setmode(GPIO.BCM)
        #REMOVE#GPIO.setup(self.GPIOport, GPIO.OUT)
        
        self.stop()
        
    def isOn(self):
        return self._powerOn
    
    def start(self):
        #REMOVE#GPIO.output(self.GPIOport, True)
        self._powerOn = True
        
    def stop(self):
        #REMOVE#GPIO.output(self.GPIOport, False)
        self._powerOn = False
