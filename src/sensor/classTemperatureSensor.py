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
    
    def getSensorData(self):
        temperature = self._getTemperature()
        
        if temperature is not None:
            return temperature
        else:
            return 20
    