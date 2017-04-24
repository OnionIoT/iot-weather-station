# helper for sending commands and receiving data from Arduino Dock

import json
import serial
import warnings

class ArduinoDock:
    def __init__(self, uart="/dev/ttyS1", baudRate=9600):
        try:
            # print "opening serial port"
            self.port = serial.Serial(port=uart, baudrate=baudRate)
        except x:
            warnings.warn("Can't open the serial port to Arduino Dock. Please close any applications using the serial port and try again.");
            raise x;
        # print "init complete"
        
    # send a command and request a JSON response
    def sendCommand(self, command):
        self.port.write(command + "\r")
        response = self.port.readline()
        # response should be encoded in json
        # TODO: enclose the json.loads call in a try/except (error handling)
        try:
            jsonResponse = json.loads(response)
        except x:
            warnings.warn("No response from Arduino Dock")
            return None
        return jsonResponse