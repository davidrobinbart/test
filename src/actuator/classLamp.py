'''
Created on 19.11.2015

@author: romanborn
'''

#REMOVE#from RPi import GPIO #@UnresolvedImport
from _thread import start_new_thread
import time

class Lamp:

    def __init__(self, port, timeout, description = ''):
        self.GPIOport = port
        self._timeout = timeout
        self.description = description
        
        self.inTimeout = False
        
        #REMOVE#GPIO.setmode(GPIO.BCM)
        #REMOVE#GPIO.setup(self.GPIOport, GPIO.OUT)
        
        #REMOVE#GPIO.output(self.GPIOport, False)
        self._powerOn = False
    
    def _timeoutSleep(self):
        time.sleep(int(self._timeout))
        self.inTimeout = False
        
    def isOn(self):
        return self._powerOn
    
    def on(self):
        if not (self.inTimeout):
            #REMOVE#GPIO.output(self.GPIOport, True)
            self._powerOn = True
        
    def off(self):
        #REMOVE#GPIO.output(self.GPIOport, False)
        self._powerOn = False

        if not (self.inTimeout):
            self.inTimeout = True
            start_new_thread(self._timeoutSleep,())
