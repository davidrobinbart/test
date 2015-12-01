'''
Created on 19.11.2015

@author: romanborn
'''

from .classSensor import Sensor

#REMOVE#import Adafruit_DHT #@UnresolvedImport

class TemperatureSensor(Sensor):
    
    def _getTemperature(self):
        #REMOVE#_, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, self.GPIOport)
        #REMOVE#return temperature
        return 20 #REMOVE#
    
    def _getHumidity(self):
        #REMOVE#humidity, _ = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, self.GPIOport)
        #REMOVE#return humidity
        return 0 #REMOVE#
    
    def _getSensorData(self):
        self.lastValue = self._getTemperature()
        
        if self.lastValue is not None:
            return self.lastValue
        else:
            return 20
    