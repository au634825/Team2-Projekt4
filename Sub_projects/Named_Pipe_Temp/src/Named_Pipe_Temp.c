/*
 ============================================================================
 Name        : Named_Pipe_Temp.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

// C program to implement one side of FIFO
// This side reads first, then reads
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include "NamedPipeCommunication.h"
#include "temperature.h"

float sensorValue = 30;

int main()
{
	// Temperature sensor
	pipeListener("/tmp/temperature", temperature, "Temp", 0, 85);
    return 0;
}
