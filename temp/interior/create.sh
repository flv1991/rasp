rrdtool create /home/pi/temp/exterior/temperatures.rrd --start N --step 60 DS:temp:GAUGE:600:0:50 RRA:AVERAGE:0.5:1:288 RRA:AVERAGE:0.5:3:672 RRA:AVERAGE:0.5:12:8880