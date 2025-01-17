#!/bin/bash

# Configure IP address range
IPRANGE="192.168.69."
IPRANGEMIN=1
IPRANGEMAX=5

for value in $(seq $IPRANGEMIN $IPRANGEMAX)}
do
    IPCheck=$IPRANGE$value
    ping -q -c 1 $IPCheck > temp ; result=$?
    if [ $result -eq 0 ]
    then
        echo $IPCheck "is alive"
    else
        echo $IPCheck "is dead"
    fi
done


function 

# Run IP scan for all IP addresses in that range, using ARP scans




#