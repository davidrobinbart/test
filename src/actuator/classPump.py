'''
Created on 19.11.2015

@author: romanborn
'''

from RPi import GPIO #@UnresolvedImport

class Pump:

    def __init__(self, port, description = ''):
        self.GPIOport = port
        self.description = description
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIOport, GPIO.OUT)
        
        self.stop()
        
    def isOn(self):
        return self._powerOn
    
    def start(self):
        GPIO.output(self.GPIOport, True)
        self._powerOn = True
        
    def stop(self):
        GPIO.output(self.GPIOport, False)
        self._powerOn = False
