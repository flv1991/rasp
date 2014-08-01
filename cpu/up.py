#cd temp/cpu
TEMPERATURE=`cat /sys/class/thermal/thermal_zone0/temp`
echo $TEMPERATURE
/usr/bin/rrdtool update /home/pi/temp/cpu/temperatures.rrd N:`/opt/vc/bin/vcgencmd measure_temp|cut -c6-9`