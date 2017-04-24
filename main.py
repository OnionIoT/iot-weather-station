# IoT Weather Station

import helpers
from time import sleep

sleepTime = 5           # seconds
eventName = "weather"   # the name of the event as registered on the cloud

# main program
def __main__():
    while True:
        # read the weather data from the arduino dock
        weatherData = helpers.getWeatherData()
        
        # send to cloud service
        if weatherData is not None:
            helpers.sendToWatson(eventName, weatherData)
        
        # sleep
        sleep(sleepTime)    
    
if __name__ == '__main__':
    __main__()