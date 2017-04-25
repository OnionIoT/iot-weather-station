# IBM IoT platform

import json
import uuid
import fileinput
import os
import re
import ibmiotf
import ibmiotf.device

# get absolute path of the config file for loading later
dirName = os.path.dirname(os.path.abspath(__file__))
defaultConfigFile = '/'.join([dirName, 'device.cfg'])

# retrieve and format the mac address, then load it into the config file
def getDeviceId():
    # get mac address
    macAddress = hex(uuid.getnode())[2:-1]
    macAddress = format(long(macAddress, 16),'012x')
    print "===================="
    print "Device ID:"
    print macAddress
    print "===================="
    
    # populate device id into device.cfg file
    file = fileinput.FileInput(defaultConfigFile, inplace=True, backup='.bak')
    for line in file:
        print re.sub(r"^id=(.*)$","id=" + macAddress, line.rstrip())
    file.close()
    print "Loaded Device ID into device.cfg."
    
    # print further instructions
    print "Enter this Device ID on the IBM Bluemix website when registering this device on the Watson IoT platform."
    print "Don't forget to add your Organization ID, Device Type, and Authorization Token to the device.cfg file!"
    return



class Watson:
    def __init__(self, deviceFile=defaultConfigFile):
        # load the config file
        # TODO: check for existence of deviceFile
        # TODO: path builder for deviceFile (so script can be called from anywhere)
        self.options = ibmiotf.device.ParseConfigFile(deviceFile)
        self.deviceClient = ibmiotf.device.Client(self.options)
        self.deviceClient.connect()
    
    # publish data to cloud
    def publishEvent(self, eventName, data):
        msg = {"d": data}
        self.deviceClient.publishEvent(eventName,"json", msg, qos=0)
        print "message published: " + json.dumps(msg)

if __name__ == '__main__':
    # load the device ID when this module is run directly
    getDeviceId()