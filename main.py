# IoT Weather Station

import helpers
from time import sleep

sleepTime = 5    # seconds

# main program
def __main__():
    while True:
        # read the weather data from the arduino dock
        weatherData = helpers.getWeatherData()
        
        # send to cloud service
        helpers.sendToCloud("weather", weatherData)
        
        # sleep
        sleep(sleepTime)    
    
if __name__ == '__main__':
    __main__()