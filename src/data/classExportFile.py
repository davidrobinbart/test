'''
Created on 19.11.2015

@author: romanborn
'''
import json
import time
import uuid

class ExportFile:

    def __init__(self, controller, 
                 contactSensor, temperatureSensor, distanceSensor, 
                 lampUV, pumpExtraWater, pumpCycleWater):
        self.path = controller.exportPath
        self.name = controller.exportFile
    
        self.exportData = {
            'station' : '',
            'stationDescription' : '',
            'data' : [
                {
                     'name' : 'waterlevel',
                     'description' : '',
                     'value' : ''
                 },
                {
                     'name' : 'temperature',
                     'description' : '',
                     'value' : ''
                 },
                {
                     'name' : 'coverstate',
                     'description' : '',
                     'value' : ''
                 },
                {
                     'name' : 'pump_cycle_water',
                     'description' : '',
                     'value' : ''
                 },
                {
                     'name' : 'pump_extra_water',
                     'description' : '',
                     'value' : ''
                 },
                {
                     'name' : 'lamp',
                     'description' : '',
                     'value' : ''
                 }
            ],
            'timestamp' : '',
            'uuid' : ''
        }
        
        self.exportData['station'] = controller.station
        self.exportData['stationDescription'] = controller.stationDescription
        
        self.exportData['data'][0]['description'] = distanceSensor.description
        self.exportData['data'][1]['description'] = temperatureSensor.description
        self.exportData['data'][2]['description'] = contactSensor.description
        self.exportData['data'][3]['description'] = pumpCycleWater.description
        self.exportData['data'][4]['description'] = pumpExtraWater.description
        self.exportData['data'][5]['description'] = lampUV.description
    
    def wirte(self, 
              contactSensor, temperatureSensor, distanceSensor, 
              lampUV, pumpExtraWater, pumpCycleWater):
        
        self.exportData['data'][0]['value'] = str(distanceSensor.lastValue)
        self.exportData['data'][1]['value'] = str(temperatureSensor.lastValue)
        self.exportData['data'][2]['value'] = contactSensor.lastValue
        
        if pumpCycleWater.isOn():
            self.exportData['data'][3]['value'] = 'On'
        else:
            self.exportData['data'][3]['value'] = 'Off'
        
        if pumpExtraWater.isOn():
            self.exportData['data'][4]['value'] = 'On'
        else:
            self.exportData['data'][4]['value'] = 'Off'
        
        if lampUV.isOn():
            self.exportData['data'][5]['value'] = 'On'
        else:
            self.exportData['data'][5]['value'] = 'Off'
 
        self.exportData['timestamp'] = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
        self.exportData['uuid'] = str(uuid.uuid4())
        
        with open(self.path + self.name, 'w') as f:
            json.dump(self.exportData, f)
        