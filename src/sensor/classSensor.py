'''
Created on 19.11.2015

@author: romanborn
'''

from RPi import GPIO #@UnresolvedImport

class Sensor:

    def __init__(self, port):
        self.GPIOport = port
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIOport, GPIO.IN)
    
    def getSensorData(self):
        pass
        
    def readData(self):
        return self.getSensorData()
    