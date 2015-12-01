'''
Created on 19.11.2015

@author: romanborn
'''

from .classSensor import Sensor

#REMOVE#from RPi import GPIO #@UnresolvedImport

class ContactSensor(Sensor):

    def _getSensorData(self):
        #REMOVE#if (GPIO.input(self.GPIOport) != 0):
        if True: #REMOVE#
            self.lastValue = 'close'
        else:
            self.lastValue = 'open'
        return self.lastValue
