'''
Created on 19.11.2015

@author: romanborn
'''

from .classSensor import Sensor
from .classTemperatureSensor import TemperatureSensor

class DistanceSensor(Sensor):

    def getSensorData(self):
        temperature = TemperatureSensor()
        return 1 + temperature.readData()
    