/*
 * temperature.c
 *
 *  Created on: 12 Feb 2021
 *      Author: volvofar
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include "temperature.h"
//#include "errorHandling.h"

float temperature() {
	char buffer[5];
	char *EHand;
	FILE *fd = fopen("/sys/bus/iio/devices/iio:device0/in_voltage0_raw", "r");
	fread(&buffer, sizeof(char), 20, fd);
	float value = strtof(buffer, &EHand);
	float temperature = (value * 1800 / 4096.0) / 10.0;

	//float temp = errorHandler(temperature, 0, 85);

	//printf("Digital value: %.2f: Celsius: %.2f\n", value, temp);
	return temperature;
	fclose(fd);
	return 0;
}

