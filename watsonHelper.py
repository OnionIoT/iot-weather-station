# IBM IoT platform

import json
import ibmiotf
import ibmiotf.device

class Watson:
    def __init__(self, deviceFile="device.cfg"):
        # load the config file
        self.options = ibmiotf.device.ParseConfigFile(deviceFile)
        self.deviceClient = ibmiotf.device.Client(self.options)
        self.deviceClient.connect()
    
    # publish data to cloud
    def publishEvent(self, eventName, data):
        msg = {"d": data}
        self.deviceClient.publishEvent(eventName,"json", msg, qos=0)
        print "message published: " + json.dumps(msg)