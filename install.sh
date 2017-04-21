#!/bin/ash
opkg update
opkg install python
opkg install python-pip

pip uninstall setuptools
pip install setuptools

# pip install ibmiotf

pip install iso8601
pip install xmltodict
pip install dicttoxml
pip install requests_toolbelt
pip install requests
pip install pytz
pip install paho_mqtt
pip install ibmiotf