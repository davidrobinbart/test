'''
Created on 19.11.2015

@author: romanborn
'''

from sensor.classContactSensor import ContactSensor
from sensor.classTemperatureSensor import TemperatureSensor
from sensor.classDistanceSensor import DistanceSensor
from actuator.classPump import Pump
from actuator.classLamp import Lamp
from data.classExportFile import ExportFile

import configparser
import time

class Controller:

    def __init__(self, file, section = 'pond', encoding = 'UTF-8'):
        self.paramFile = file
        self.paramSection = section
        self.paramEncoding = encoding
    
    def _readConfig(self):
        config = configparser.ConfigParser()
        config.read(self.paramFile, self.paramEncoding)
        
        self.lampTimeout = config[self.paramSection]['lamp_timeout']
        self.exportPath = config[self.paramSection]['export_path']
        self.exportFile = config[self.paramSection]['export_file']
        self.station = config[self.paramSection]['station']
        self.stationDescription = config[self.paramSection]['station_description']
        
    def run(self):
        self._readConfig()
        
        exportFile = ExportFile(self.exportPath, self.exportFile)
        
        contactSensor = ContactSensor(17)
        temperatureSensor = TemperatureSensor(4)
        distanceSensor = DistanceSensor(22, 27, temperatureSensor)
        
        lampUV = Lamp(18)
        pumpExtraWater = Pump(23)
        pumpCycleWater = Pump(24)
        
        counter = 0
        distanceSum = 0
        
        while True:
            counter += 1
            distanceSum += distanceSensor.readData()
 
            print('contact ' + contactSensor.readData())
            print('temperature ' + str(temperatureSensor.readData()))
            print('lamp on? ' + str(lampUV.isOn()))
            print('pump extra water on? ' + str(pumpExtraWater.isOn()))
            print('pump cycle water on? ' + str(pumpCycleWater.isOn()))
            
            if (counter == 30):    
                print('distance ' + str((distanceSum / 30)))
        
                exportFile.wirte({'station':self.station, 'stationDesciption':self.stationDescription})

            if (counter > 30): 
                counter = 0
                distanceSum = 0
        
            print('---')
            time.sleep(1)
        
        
        