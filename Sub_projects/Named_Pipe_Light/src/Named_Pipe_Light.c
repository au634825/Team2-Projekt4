/*
 ============================================================================
 Name        : Named_Pipe_Light.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include "NamedPipeCommunication.h"
#include "LUXSensor.h"

//float sensorValue = 30;

int main()
{
	// Temperature sensor
	pipeListener("/tmp/irradiance", lightSensor, "Light Intensity", 0, 100000);
    return 0;
}

