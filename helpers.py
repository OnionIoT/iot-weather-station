# helpers file containing block-level functions used in main

from arduinoDockHelper import ArduinoDock
from watsonHelper import Watson
from configHelper import config

arduinoDock = ArduinoDock()
watson = Watson()

def getWeatherData():
    response = arduinoDock.sendCommand('r')
    return response
    
def sendToCloud(eventName, data):
    watson.publishEvent(eventName, data)