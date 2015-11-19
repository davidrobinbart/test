'''
Created on 19.11.2015

@author: romanborn
'''

from controller.classController import Controller

if __name__ == '__main__':
    controller = Controller('params.ini')
    controller.run()