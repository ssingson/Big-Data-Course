#!/bin/sh
../start.sh

/usr/local/hadoop/bin/hdfs dfs -rm -r /Lab1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Lab1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Lab1/output2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Lab1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../mapreduce-test-data/access.log /Lab1/input/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../Lab1/mapper_part2.py -mapper ../Lab1/mapper_part2.py 3 8 \
-file ../Lab1/reducer.py -reducer ../Lab1/reducer.py \
-input /Lab1/input/* -output /Lab1/output/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../Lab1/mapper2.py -mapper ../Lab1/mapper2.py \
-file ../Lab1/reducer2.py -reducer ../Lab1/reducer2.py \
-input /Lab1/output/part-00000 -output /Lab1/output2/

#/usr/local/hadoop/bin/hdfs dfs -cat /Lab1/output/part-00000

/usr/local/hadoop/bin/hdfs dfs -cat /Lab1/output2/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /Lab1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Lab1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Lab1/output2/
../stop.sh
