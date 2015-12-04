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
        
        self.distanceMin = int(config[self.paramSection]['distance_min'])
        self.distanceMax = int(config[self.paramSection]['distance_max'])
        self.distanceIntervall = int(config[self.paramSection]['distance_intervall'])
        
        self.exportPath = config[self.paramSection]['export_path']
        self.exportFile = config[self.paramSection]['export_file']
        self.exportFileIntervall = int(config[self.paramSection]['export_file_intervall'])
        
        self.station = config[self.paramSection]['station']
        self.stationDescription = config[self.paramSection]['station_description']
        self.sensorContactDescription = config[self.paramSection]['sensor_coverstate_description']
        self.sensorTemperatureDescription = config[self.paramSection]['sensor_temperature_description']
        self.sensorDistanceDescription = config[self.paramSection]['sensor_waterevel_description']
        self.actuatorLampDescription = config[self.paramSection]['actuator_lamp_description']
        self.actuatorExtraWaterDescription = config[self.paramSection]['actuator_pump_extra_water_description']
        self.actuatorCycleWaterDescription = config[self.paramSection]['actuator_pump_cylce_water_description']

        self.gpioContact = int(config[self.paramSection]['gpio_contact'])
        self.gpioTemperature = int(config[self.paramSection]['gpio_temperature'])
        self.gpioDistanceTrigger = int(config[self.paramSection]['gpio_distance_trigger'])
        self.gpioDistanceEcho = int(config[self.paramSection]['gpio_distance_echo'])
        self.gpioLamp = int(config[self.paramSection]['gpio_lamp'])
        self.gpioPumpExtraWater = int(config[self.paramSection]['gpio_pump_extra_water'])
        self.gpioPumpCycleWater = int(config[self.paramSection]['gpio_pump_cycle_water'])
        
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
        actualDistance = (self.distanceMin + self.distanceMax) / 2
        
        while True:
            counter += 1
            distanceSum += distanceSensor.readData()
            
            ''' calculate distance '''
            if (counter == self.distanceIntervall):    
                actualDistance = distanceSum / self.distanceIntervall
                counter = 0
                distanceSum = 0


            ''' check states '''        
            if (contactSensor.readData() == 'open'):
                if (lampUV.isOn()): 
                    lampUV.off()
                if (pumpCycleWater.isOn()): 
                    pumpCycleWater.stop()
                if (pumpExtraWater.isOn()): 
                    pumpExtraWater.stop()
            elif (actualDistance >= self.distanceMax):
                if (lampUV.isOn()): 
                    lampUV.off()
                if (pumpCycleWater.isOn()):
                    pumpCycleWater.stop()
                if not (pumpExtraWater.isOn()):
                    pumpExtraWater.start()
            else:
                if not (lampUV.isOn()):
                    lampUV.on()
                if not (pumpCycleWater.isOn()):
                    pumpCycleWater.start()
                if ((actualDistance <= self.distanceMin) and (pumpExtraWater.isOn())):
                    pumpExtraWater.stop()


            ''' write file '''
            if (counter % self.exportFileIntervall == 0):
                exportFile.wirte(contactSensor, temperatureSensor, distanceSensor, 
                                 lampUV, pumpExtraWater, pumpCycleWater)


            ''' debug start '''
            print(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
            print('contact ' + contactSensor.lastValue)
            print('temperature ' + str(temperatureSensor.lastValue))
            print('lamp on? ' + str(lampUV.isOn()))
            print('pump extra water on? ' + str(pumpExtraWater.isOn()))
            print('pump cycle water on? ' + str(pumpCycleWater.isOn()))
            print('actual distance ' + str(actualDistance))
            print(str(counter) + ' ' + str(self.distanceIntervall))
            print('----------------------------------------')
            ''' debug end '''

            time.sleep(0.3)
        
        
        