# Set the earliest hour for the filter
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

#print earliest and latest time
echo $firsttime $lasttime

#../stop.sh
