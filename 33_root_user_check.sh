#/bin/bash

if [[ $UID -eq 0 ]]
then
	echo "this is root user"
else
	echo "not root"
fi
