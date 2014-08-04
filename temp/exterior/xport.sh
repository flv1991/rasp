rrdtool xport -s now-3h -e now --step 60 DEF:cputemp=cputemp.rrd:cputemp:AVERAGE XPORT:cputemp:"temperatura" > temps24h.xml
