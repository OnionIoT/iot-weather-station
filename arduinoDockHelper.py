# helper for sending commands and receiving data from Arduino Dock

import json
import serial

class ArduinoDock:
    def __init__(self, uart="/dev/ttyS1", baudRate=9600):
        try:
            self.port = serial.Serial(port=uart, baudrate=baudRate)
        except x:
            warnings.warn("Can't open the serial port to Arduino Dock. Please close any applications using the serial port and try again.");
            raise x;
        
    # send a command and request a JSON response
    def sendCommand(self, command):
        self.port.write(command + "\r")
        response = self.port.readline()
        # response should be encoded in json
        return json.loads(response)
        