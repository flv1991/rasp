#cd temp/cpu
TEMPERATURE=`cat /sys/bus/w1/devices/28-*/w1_slave | sed -n 's/^.*\(t=[^ ]*\).*/\1/p' | sed 's/t=//' | awk '{x=$1}END{print(x/1000)}'`
echo $TEMPERATURE
/usr/bin/rrdtool update /home/pi/temp/interior/temperatures.rrd N:`cat /sys/bus/w1/devices/28-*/w1_slave | sed -n 's/^.*\(t=[^ ]*\).*/\1/p' | sed 's/t=//' | awk '{x=$1}END{print(x/1000)}'`