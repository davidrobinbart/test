'''
Created on 19.11.2015

@author: romanborn
'''

from RPi import GPIO #@UnresolvedImport

class Pump:

    def __init__(self, port):
        self.GPIOport = port
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIOport, GPIO.OUT)
        
        self.stop()
        
    def isOn(self):
        return self.powerOn
    
    def start(self):
        GPIO.output(self.GPIOport, True)
        self.powerOn = True
        
    def stop(self):
        GPIO.output(self.GPIOport, False)
        self.powerOn = False
