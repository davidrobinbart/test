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
        
        self.distanceMin = config[self.paramSection]['distance_min']
        self.distanceMax = config[self.paramSection]['distance_max']
        self.distanceIntervall = config[self.paramSection]['distance_intervall']
        
        self.exportPath = config[self.paramSection]['export_path']
        self.exportFile = config[self.paramSection]['export_file']
        self.exportFileIntervall = config[self.paramSection]['export_file_intervall']
        
        self.station = config[self.paramSection]['station']
        self.stationDescription = config[self.paramSection]['station_description']
        self.sensorContactDescription = config[self.paramSection]['sensor_coverstate_description']
        self.sensorTemperatureDescription = config[self.paramSection]['sensor_temperature_description']
        self.sensorDistanceDescription = config[self.paramSection]['sensor_waterevel_description']
        self.actuatorLampDescription = config[self.paramSection]['actuator_lamp_description']
        self.actuatorExtraWaterDescription = config[self.paramSection]['actuator_pump_extra_water_description']
        self.actuatorCycleWaterDescription = config[self.paramSection]['actuator_pump_cylce_water_description']

        self.gpioContact = config[self.paramSection]['gpio_contact']
        self.gpioTemperature = config[self.paramSection]['gpio_temperature']
        self.gpioDistanceTrigger = config[self.paramSection]['gpio_distance_trigger']
        self.gpioDistanceEcho = config[self.paramSection]['gpio_distance_echo']
        self.gpioLamp = config[self.paramSection]['gpio_lamp']
        self.gpioPumpExtraWater = config[self.paramSection]['gpio_pump_extra_water']
        self.gpioPumpCycleWater = config[self.paramSection]['gpio_pump_cycle_water']
        
    def run(self):
        self._readConfig()
        
        contactSensor = ContactSensor(self.gpioContact, self.sensorContactDescription)
        temperatureSensor = TemperatureSensor(self.gpioTemperature, self.sensorTemperatureDescription)
        distanceSensor = DistanceSensor(self.gpioDistanceTrigger, self.gpioDistanceEcho, temperatureSensor, self.sensorDistanceDescription)
        
        lampUV = Lamp(self.gpioLamp, self.lampTimeout, self.actuatorLampDescription)
        pumpExtraWater = Pump(self.gpioPumpExtraWater, self.actuatorExtraWaterDescription)
        pumpCycleWater = Pump(self.gpioPumpCycleWater, self.actuatorCycleWaterDescription)
        
        exportFile = ExportFile(self, 
                                contactSensor, temperatureSensor, distanceSensor, 
                                lampUV, pumpExtraWater, pumpCycleWater)
        
        ''' start up '''
        if (contactSensor.readData() == 'close'):
            lampUV.on()
            pumpCycleWater.start()
            pumpExtraWater.stop()
        
        counter = 0
        distanceSum = 0
        actualDistance = (int(self.distanceMin) + int(self.distanceMax)) / 2
        
        while True:
            counter += 1
            distanceSum += distanceSensor.readData()
            
            ''' calculate distance '''
            if (counter == int(self.distanceIntervall)):    
                actualDistance = distanceSum / int(self.distanceIntervall)
                counter = 0
                distanceSum = 0


            ''' check states '''        
            if (contactSensor.readData() == 'open'):
                lampUV.off()
                pumpCycleWater.stop()
                pumpExtraWater.stop()
            elif (actualDistance <= int(self.distanceMin)):
                lampUV.off()
                pumpCycleWater.stop()
                pumpExtraWater.start()
            else:
                lampUV.on()
                pumpCycleWater.start()
                if (actualDistance >= int(self.distanceMax)): pumpExtraWater.stop()


            ''' write file '''
            if (counter % int(self.exportFileIntervall) == 0):
                exportFile.wirte(contactSensor, temperatureSensor, distanceSensor, 
                                 lampUV, pumpExtraWater, pumpCycleWater)


            ''' debug start '''
            print('contact ' + contactSensor.readData())
            print('temperature ' + str(temperatureSensor.readData()))
            print('lamp on? ' + str(lampUV.isOn()))
            print('pump extra water on? ' + str(pumpExtraWater.isOn()))
            print('pump cycle water on? ' + str(pumpCycleWater.isOn()))
            print('actual distance ' + str(actualDistance))
            print(str(counter) + ' ' + self.distanceIntervall)
            print('----------------------------------------')
            ''' debug end '''

            time.sleep(1)
        
        
        