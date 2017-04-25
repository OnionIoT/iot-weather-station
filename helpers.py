# helpers file containing block-level functions used in main

from arduinoDockHelper import ArduinoDock
from watsonHelper import Watson

arduinoDock = ArduinoDock()
watson = Watson()

def getWeatherData():
    response = arduinoDock.sendCommand('r')
    return response
    
def sendToWatson(eventName, data):
    watson.publishEvent(eventName, data)