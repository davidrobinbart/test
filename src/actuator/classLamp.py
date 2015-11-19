'''
Created on 19.11.2015

@author: romanborn
'''

class Lamp:

    def __init__(self):
        pass
        
    def isOn(self):
        return self.powerOn
    
    def on(self):
        self.powerOn = True
        
    def off(self):
        self.powerOn = False
