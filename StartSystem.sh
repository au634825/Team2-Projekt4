#!/bin/bash

# Team2 Project 4 - start up script.

echo "Starting Receiver.."
python3 ./MainCode/src/Receiver.py &
echo "Receiver started"

echo "Starting Transmitter.."
python3 ./MainCode/src/Transmitter.py &
echo "Transmitter started"
