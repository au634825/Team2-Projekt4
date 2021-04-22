echo "Starting Light intensity controller.."
./Sub_projects/Named_Pipe_Light_intensity/Named_Pipe_Light_intensity &
LightIntensityPID=$!
echo "LightIntensityPID pid: $LightIntensityPID"
echo "Light intensity controller started"
sleep 1

echo ""
echo "All process started"

echo "Enter to terminate:"
read -r var
kill $LightIntensityPID
echo "Process terminated"