#!/bin/sh
../start.sh



#test test test
/usr/local/hadoop/bin/hdfs dfs -rm -r /input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /input/

/usr/local/hadoop/bin/hdfs dfs -copyFromLocal parking_sampled.csv /input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input /input/* -output /input/output/ 

/usr/local/hadoop/bin/hdfs dfs cp /input/output/ /output2/ 

# checks if the clusters are the same (after the first reclustering) or if less than 50 reclusters
while (([/input/output/ != /output2/] and n == 0) || n < 50)
do 
  /usr/local/hadoop/bin/hdfs dfs cp /output2/ /input/output/
  /usr/local/hadoop/bin/hdfs dfs -rm -r /output2/
  
  /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
  -file mapper2.py -mapper mapper2.py \
  -file reducer2.py -reducer reducer2.py \
  -input /input/* \
  -input /output/* \
  -inputformat org.apache.hadoop.mapred.TextInputFormat \
  -output /output2/
done 





/usr/local/hadoop/bin/hdfs dfs -cat /output2/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /output2/
../stop.sh
