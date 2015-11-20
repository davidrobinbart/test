'''
Created on 19.11.2015

@author: romanborn
'''

from RPi import GPIO #@UnresolvedImport

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

class Lamp:

    def __init__(self):
        pass
        
    def isOn(self):
        return self.powerOn
    
    def on(self):
        GPIO.output(18, True)
        self.powerOn = True
        
    def off(self):
        GPIO.output(18, False)
        self.powerOn = False
