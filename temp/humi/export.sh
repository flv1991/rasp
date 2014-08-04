rrdtool xport -s now-3h -e now --step 60 DEF:humi=humi.rrd:humi:AVERAGE XPORT:humi:"humidity" > temps24h.xml

