#cd temp/cpu
TEMPERATURE=`cat /sys/bus/w1/devices/28-*/w1_slave | grep  -E -o ".{0,0}t=.{0,5}" | cut -c 3-`
echo $TEMPERATURE
/usr/bin/rrdtool update /home/pi/temp/exterior/temperatures.rrd N:`cat /sys/bus/w1/devices/28-*/w1_slave | sed -n 's/^.*\(t=[^ ]*\).*/\1/p' | sed 's/t=//' | awk '{x=$1}END{print(x/1000)}'`
