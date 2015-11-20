'''
Created on 19.11.2015

@author: romanborn
'''

from .classSensor import Sensor

from RPi import GPIO #@UnresolvedImport
import time

class DistanceSensor(Sensor):

    def __init__(self, trigger, echo, temperatureSensor):
        self.GPIOtrigger = trigger
        self.GPIOecho = echo
        self.temperatureSensor = temperatureSensor
        
        GPIO.setup(self.GPIOtrigger, GPIO.OUT)
        GPIO.setup(self.GPIOecho, GPIO.IN)

    def _readDistance(self):
        GPIO.output(self.GPIOtrigger, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIOtrigger, False)
        
        startTime = time.time()
        stopTime= time.time()
        
        temperature = self.temperatureSensor.readData()
        
        while GPIO.input(self.GPIOecho) == 0:
            startTime = time.time()
        
        while GPIO.input(self.GPIOecho) == 1:
            stopTime = time.time()
        
        timeElapsed = startTime - stopTime
        
        # calculate distance from time elapsed and temperature in centimeters (*100)
        return (timeElapsed * (331.5 + 0.6 * temperature) / 2) * 100

    def getSensorData(self):
        return self.temperatureSensor.readData()
    