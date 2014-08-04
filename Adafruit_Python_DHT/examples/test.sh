DHT='/home/pi/Adafruit_Python_DHT/examples'
Adafruit_DHT 11 27 > $DHT
cat $DHT
hum=`cat $DHT |cut -d , -s -f 2- |tr -cd '0-9\012'`
echo $hum
tmp=`cat $DHT |cut -d , -s -f -1 |tr -cd '0-9\012'`
echo $tmp
