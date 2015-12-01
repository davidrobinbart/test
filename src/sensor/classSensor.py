'''
Created on 19.11.2015

@author: romanborn
'''

#REMOVE#from RPi import GPIO #@UnresolvedImport

class Sensor:

    def __init__(self, port, description = ''):
        self.GPIOport = port
        self.description = description
        self.lastValue = None
        
        #REMOVE#GPIO.setmode(GPIO.BCM)
        #REMOVE#GPIO.setup(self.GPIOport, GPIO.IN)
    
    def _getSensorData(self):
        pass
        
    def readData(self):
        return self._getSensorData()
    
    def getLastValue(self):
        return self.lastValue