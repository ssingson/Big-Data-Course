#!/bin/sh
../start.sh




/usr/local/hadoop/bin/hdfs dfs -rm -r /input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output2/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output3/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /input/

/usr/local/hadoop/bin/hdfs dfs curl -o /input/parking_violations.csv https://data.cityofnewyork.us/api/views/pvqr-7yc4/rows.csv?accessType=DOWNLOAD
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper.py -mapper mapper.py 2000\
-file reducer.py -reducer reducer.py \
-input /input/* -output /input/output/ 

/usr/local/hadoop/bin/hdfs dfs cp /input/output/ /output2/ 

# checks if the clusters are the same (after the first reclustering) or if less than 50 reclusters
while (([/input/output/ != /output2/] and n == 0) || n < 50)
do 
  /usr/local/hadoop/bin/hdfs dfs cp /output2/ /input/output/
  /usr/local/hadoop/bin/hdfs dfs -rm -r /output2/
  
  /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
  -file mapper2.py -mapper mapper2.py\
  -file reducer2.py -reducer reducer2.py \
  -input /input/* \
  -input /output/* \
  -inputformat org.apache.hadoop.mapred.TextInputFormat \
  -output /output2/
done 

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper - black car.py -mapper mapper - black car.py\
-file reducer - black car.py -reducer reducer - black car.py \
-input /output2/* -output /input/output3/ 

/usr/local/hadoop/bin/hdfs dfs -cat /output3/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output2/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output3/
../stop.sh
