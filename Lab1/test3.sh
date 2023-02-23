#!/bin/sh
#../start.sh


#while ! [[ $yournumber =~ $re ]] || [$firsttime -gt 24] && [$firsttime -lt 0]:
#  echo What is the earliest time you want? 
#  read firsttime
#  if ! [[ $yournumber =~ $re ]] || [$firsttime -gt 24] && [$firsttime -lt 0]: 
#    echo Please insert an integer between 0 and 24. 
declare -i lasttime=25

while ((firsttime < 0)) || ((firsttime > 24))
do
  echo 'What is the earliest hour you want?' 
  read lasttime
  if ((firsttime < 0)) || ((firsttime > 24))
  then
    echo 'Please insert an integer between 0 and 24.' 
  fi
done

while ((lasttime < 0)) || ((lasttime > 24))
do
  echo 'What is the latest hour you want?' 
  read lasttime
  if ((lasttime < 0)) || ((lasttime > 24))
  then
    echo 'Please insert an integer between 0 and 24.' 
  fi
done

echo $firsttime $lasttime

#../stop.sh
