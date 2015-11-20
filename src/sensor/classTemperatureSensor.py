'''
Created on 19.11.2015

@author: romanborn
'''

from .classSensor import Sensor

import Adafruit_DHT #@UnresolvedImport

class TemperatureSensor(Sensor):
    
    def getSensorData(self):
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, self.GPIOport)
        
        if temperature is not None:
            return temperature
        else:
            return 20
    