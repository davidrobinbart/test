'''
Created on 19.11.2015

@author: romanborn
'''

from .classSensor import Sensor

class TemperatureSensor(Sensor):

    def getSensorData(self):
        return 2
    