'''
Created on 19.11.2015

@author: romanborn
'''

from .classSensor import Sensor

from RPi import GPIO #@UnresolvedImport

class ContactSensor(Sensor):

    def getSensorData(self):
        if (GPIO.input(self.GPIOport) != 0):
            return 'open'
        else:
            return 'closed'
