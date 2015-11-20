'''
Created on 19.11.2015

@author: romanborn
'''

from RPi import GPIO #@UnresolvedImport

class Lamp:

    def __init__(self, port):
        self.GPIOport = port
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIOport, GPIO.OUT)
        
        self.off()
        
    def isOn(self):
        return self.powerOn
    
    def on(self):
        GPIO.output(self.GPIOport, True)
        self.powerOn = True
        
    def off(self):
        GPIO.output(self.GPIOport, False)
        self.powerOn = False
