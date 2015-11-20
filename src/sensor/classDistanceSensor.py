'''
Created on 19.11.2015

@author: romanborn
'''

from .classSensor import Sensor

class DistanceSensor(Sensor):

    def __init__(self, temperatureSensor):
        self.temperatureSensor = temperatureSensor

    def getSensorData(self):
        return 1 + self.temperatureSensor.readData()
    