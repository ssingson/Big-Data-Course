#!/bin/sh
../start.sh

declare -i firsttime=25

while ((firsttime < 0)) || ((firsttime > 24))
do
  echo 'What is the earliest hour you want?' 
  read firsttime
  if ((firsttime < 0)) || ((firsttime > 24))
  then
    echo 'Please insert an integer between 0 and 24.' 
  fi
done
echo 

# Set the latest hour for the filter
declare -i lasttime=25


while ((lasttime < 0)) || ((lasttime > 24))
do
  echo 'What is the latest hour you want?' 
  read lasttime
  if ((lasttime < 0)) || ((lasttime > 24))
  then
    echo 'Please insert an integer between 0 and 24.' 
  fi
done
echo

#print earliest and latest time
echo The top IPs will be between $firsttime:00 and $lasttime:00.
echo 

/usr/local/hadoop/bin/hdfs dfs -rm -r /Lab1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Lab1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Lab1/output2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /Lab1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../mapreduce-test-data/access.log /Lab1/input/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../Lab1/mapper_part2.py -mapper '../Lab1/mapper_part2.py' '$firsttime $lasttime' \
-file ../Lab1/reducer.py -reducer ../Lab1/reducer.py \
-input /Lab1/input/* -output /Lab1/output/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../Lab1/mapper2.py -mapper ../Lab1/mapper2.py \
-file ../Lab1/reducer2.py -reducer ../Lab1/reducer2.py \
-input /Lab1/output/part-00000 -output /Lab1/output2/


/usr/local/hadoop/bin/hdfs dfs -cat /Lab1/output2/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /Lab1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Lab1/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /Lab1/output2/
../stop.sh
