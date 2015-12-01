'''
Created on 19.11.2015

@author: romanborn
'''

from .classSensor import Sensor

from RPi import GPIO #@UnresolvedImport
import time

class DistanceSensor(Sensor):

    def __init__(self, trigger, echo, temperatureSensor, description = ''):
        self.GPIOtrigger = trigger
        self.GPIOecho = echo
        self.temperatureSensor = temperatureSensor
        self.description = description
        
        GPIO.setup(self.GPIOtrigger, GPIO.OUT)
        GPIO.setup(self.GPIOecho, GPIO.IN)

    def _readDistance(self):
        temperature = self.temperatureSensor.readData()
  
        ''' time critical section - begin '''      
        GPIO.output(self.GPIOtrigger, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIOtrigger, False)
        
        startTime = time.time()
        stopTime= time.time()
        
        while GPIO.input(self.GPIOecho) == 0:
            startTime = time.time()
        
        while GPIO.input(self.GPIOecho) == 1:
            stopTime = time.time()
        ''' time critical section -end '''  
       
        ''' calculate distance from time elapsed and temperature in centimeters (* 100) '''
        return ((stopTime - startTime) * (331.5 + 0.6 * temperature) / 2) * 100

    def _getSensorData(self):
        self.lastValue = self._readDistance()
        return self.lastValue
    