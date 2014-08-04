result=$(sudo /home/pi/temp/humi/11.py)
echo $result
/usr/bin/rrdtool update /home/pi/temp/humi/humi.rrd N:$result


