/*
 ============================================================================
 Name        : Named_Pipe.c
 Author      : Ricky Schultz
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

float sensorValue = 30;

int main()
{
	pipeListener("/tmp/Temp");
    return 0;
}

