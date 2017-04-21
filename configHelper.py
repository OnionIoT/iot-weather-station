# configuration loader

import os
import json

dirName = os.path.dirname(os.path.abspath(__file__))
# read the config file relative to the script location
with open( '/'.join([dirName, 'config.json']) ) as f:
    config = json.load(f)