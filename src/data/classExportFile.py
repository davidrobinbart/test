'''
Created on 19.11.2015

@author: romanborn
'''
import json
import time
import uuid

class ExportFile:

    def __init__(self, path, name):
        self.path = path
        self.name = name
    
    def wirte(self, data):
        
        exportData = {
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
                     'name' : 'pump1',
                     'description' : '',
                     'value' : ''
                 },
                {
                     'name' : 'pump2',
                     'description' : '',
                     'value' : ''
                 }
            ],
            'timestamp' : '',
            'uuid' : ''
            }
        
        exportData['station'] = data['station']
        exportData['timestamp'] = time.time()
        exportData['uuid'] = str(uuid.uuid4())
            
        with open(self.path + self.name, 'w') as f:
            json.dump(exportData, f)
        