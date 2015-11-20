'''
Created on 19.11.2015

@author: romanborn
'''

from sensor.classContactSensor import ContactSensor
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
        
        export = ExportFile(self.exportPath, self.exportFile)
        export.wirte({'station':self.station, 'stationDesciption':self.stationDescription})
        
        contact = ContactSensor()
        
        distance = DistanceSensor()
        
        lampUV = Lamp(18)
        lampUV.on()
        time.sleep(3)
        lampUV.off()
        
        time.sleep(3)
        
        pumpExtraWater = Pump(23)
        pumpExtraWater.start()
        time.sleep(3)
        pumpExtraWater.stop()

        time.sleep(3)

        pumpCycleWater = Pump(24)
        pumpCycleWater.start()
        time.sleep(3)
        pumpCycleWater.stop()
        
        
        
        print(contact.readData())
        print(distance.readData())
        print(lampUV.isOn())
        print(pumpExtraWater.isOn())
        print(pumpCycleWater.isOn())
        
        
        