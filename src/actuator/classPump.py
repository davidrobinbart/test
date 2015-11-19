'''
Created on 19.11.2015

@author: romanborn
'''

class Pump:

    def __init__(self):
        pass
        
    def isOn(self):
        return self.powerOn
    
    def start(self):
        self.powerOn = True
        
    def stop(self):
        self.powerOn = False
