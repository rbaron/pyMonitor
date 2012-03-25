#!/bin/bash

# Program full path... Put the full path of the pyMonitor.py file!
# It should be executable. (chmod +x pyMonitor.py)
EXE="[YOUR FULL PATH HERE]/pyMonitor.py"

# Check if there is alread an instance of pyMonitor running
N=`ps aux | grep -c $EXE`

#echo "Ouput from grep: $OUTPUT"

# The number of matches should be 1 when the program is not running and 2 when it is running

if [ $N -eq 1 ]; then
	#Execute
	echo "Executing $EXE"
	$EXE &

else
	# Do nothing
	echo "There is already an instance of $EXE running."
fi


	
