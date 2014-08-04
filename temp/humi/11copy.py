#!/usr/bin/python
import rrdtool
import os
import sys
import Adafruit_DHT
sensor = 11
pin = 27
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
print humidity
#os.system("/usr/bin/rrdtool update /home/pi/temp/humi/humi.rrd N: Adafruit_DHT.read_retry(11, 27)")
#rrdtool.update('humi.rrd', 'N:%s' % humidity)
#/usr/bin/rrdtool update /home/pi/temp/humi/humi.rrd N:`Adafruit_DHT.read_retry(11, 27)`
rrdtool.update('/home/pi/temp/humi/humi.rrd', 'N:%s' %humidity)
#ret = rrd_update('humi.rrd', 'N:%s' %humidity)
