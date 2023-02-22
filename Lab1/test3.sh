#!/bin/sh
../start.sh

#re='^[0-9]+$'

#while ! [[ $yournumber =~ $re ]] || [$firsttime -gt 24] && [$firsttime -lt 0]:
#  echo What is the earliest time you want? 
#  read firsttime
#  if ! [[ $yournumber =~ $re ]] || [$firsttime -gt 24] && [$firsttime -lt 0]: 
#    echo Please insert an integer between 0 and 24. 
declare -i lasttime=25
#while [$lasttime -gt 24] || [$lasttime -lt 0]:
#  echo 'What is the latest time you want?' 
#  read lasttime

echo $lasttime

../stop.sh
