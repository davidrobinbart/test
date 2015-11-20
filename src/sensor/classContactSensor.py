'''
Created on 19.11.2015

@author: romanborn
'''

from .classSensor import Sensor

from RPi import GPIO #@UnresolvedImport

class ContactSensor(Sensor):

    def getSensorData(self):
        return (GPIO.input(self.GPIOport) == 0)
