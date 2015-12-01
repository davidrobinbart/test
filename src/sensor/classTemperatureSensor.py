'''
Created on 19.11.2015

@author: romanborn
'''

from .classSensor import Sensor

import Adafruit_DHT #@UnresolvedImport

class TemperatureSensor(Sensor):
    
    def _getTemperature(self):
        _, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, self.GPIOport)
        return temperature
    
    def _getHumidity(self):
        humidity, _ = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, self.GPIOport)
        return humidity
    
    def _getSensorData(self):
        self.lastValue = self._getTemperature()
        
        if self.lastValue is not None:
            return self.lastValue
        else:
            return 20
    