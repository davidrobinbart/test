'''
Created on 19.11.2015

@author: romanborn
'''

from .classSensor import Sensor

#REMOVE#from RPi import GPIO #@UnresolvedImport
import time

class DistanceSensor(Sensor):

    def __init__(self, trigger, echo, temperatureSensor, description = ''):
        self.GPIOtrigger = trigger
        self.GPIOecho = echo
        self.temperatureSensor = temperatureSensor
        self.description = description
        
        #REMOVE#GPIO.setup(self.GPIOtrigger, GPIO.OUT)
        #REMOVE#GPIO.setup(self.GPIOecho, GPIO.IN)

    def _readDistance(self):
        temperature = self.temperatureSensor.readData()
  
        ''' time critical section - begin '''      
        #REMOVE#GPIO.output(self.GPIOtrigger, True)
        time.sleep(0.00001)
        #REMOVE#GPIO.output(self.GPIOtrigger, False)
        
        startTime = time.time()
        stopTime= time.time()
        
        #REMOVE#while GPIO.input(self.GPIOecho) == 0:
        #REMOVE#   startTime = time.time()
        
        #REMOVE#while GPIO.input(self.GPIOecho) == 1:
        #REMOVE#   stopTime = time.time()
        ''' time critical section -end '''  
       
        ''' calculate distance from time elapsed and temperature in centimeters (* 100) '''
        return ((stopTime - startTime) * (331.5 + 0.6 * temperature) / 2) * 100

    def _getSensorData(self):
        self.lastValue = self._readDistance()
        return self.lastValue
    