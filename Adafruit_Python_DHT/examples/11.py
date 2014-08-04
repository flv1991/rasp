#!/usr/bin/python

import sys
import Adafruit_DHT
sensor = 11
pin = 27
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
return humidity

