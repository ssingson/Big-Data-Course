#!/bin/sh
../start.sh
#test test test
/usr/local/hadoop/bin/hdfs dfs -rm -r /input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /input/
curl -o /input/parking_violations.csv https://data.cityofnewyork.us/api/views/pvqr-7yc4/rows.csv?accessType=DOWNLOAD
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file /mapper.py -mapper /mapper.py \
-file /reducer.py -reducer /reducer.py \
-input /input/* -output /output/

/usr/local/hadoop/bin/hdfs dfs -cat /output2/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output2/
../stop.sh
