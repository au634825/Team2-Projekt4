#!/bin/bash

# Team2 Project 4 - start up script.

cd /home/team2/Team2-Projekt4

echo "Starting Receiver.."
python3 /home/team2/Team2-Projekt4/MainCode/src/Receiver.py &
ReceiverPID=$!
echo "Receiver pid: $ReceiverPID"
echo "Receiver started"
sleep 1

echo "Starting Transmitter.."
python3 /home/team2/Team2-Projekt4/MainCode/src/Transmitter.py &
TransmitterPID=$!
echo "TransmitterPID pid: $TransmitterPID"
echo "Transmitter started"
sleep 1

echo "Starting Multimeter sensor.."
python3 /home/team2/Team2-Projekt4/MainCode/src/INA260Multimeter/adafruit.py &
MultimeterPID=$!
echo "MultimeterPID pid: $TransmitterPID"
echo "Multimeter started"
sleep 1

echo "Starting Light sensor.."
/home/team2/Team2-Projekt4/Sub_projects/Named_Pipe_Light/Named_Pipe_Light &
LightSensorPID=$!
echo "LightSensorPID pid: $LightSensorPID"
echo "Light sensor started"
sleep 1

echo "Starting Temperature sensor.."
/home/team2/Team2-Projekt4/Sub_projects/Named_Pipe_Temp/Named_Pipe_Temp &
TempSensorPID=$!
echo "TempSensorPID pid: $TempSensorPID"
echo "Temperature sensor started"
sleep 1

echo "Starting Light intensity controller.."
config-pin P9_21 pwm &
echo 1 > /sys/devices/platform/ocp/48300000.epwmss/48300200.pwm/pwm/pwmchip1/export &
/home/team2/Team2-Projekt4/Sub_projects/Named_Pipe_Light_intensity/Named_Pipe_Light_intensity &
LightIntensityPID=$!
echo "LightIntensityPID pid: $LightIntensityPID"
echo "Light intensity controller started"
sleep 1

echo "Starting load potentiometer controller.."
python3 /home/team2/Team2-Projekt4/MainCode/src/servo_pot/servo_pot_styring.py &
LoadPID=$!
echo "LoadPID pid: $LoadPID"
echo "Load potentiometer controller started"
sleep 1

echo "Starting panel angle controller.."
python3 /home/team2/Team2-Projekt4/MainCode/src/servo_solpanel/servo_panel_styring.py &
PanelAnglePID=$!
echo "PanelAnglePID pid: $PanelAnglePID"
echo "panel angle controller started"
sleep 1

echo ""
echo "All process started"

rm /tmp/StartSystem
mkfifo /tmp/StartSystem
echo "Enter to terminate in NamedPipe:"
cat /tmp/StartSystem

kill $ReceiverPID
kill $TransmitterPID
kill $MultimeterPID
kill $LightSensorPID
kill $TempSensorPID
kill $LightIntensityPID
kill $LoadPID
kill $PanelAnglePID
echo "Process terminated"