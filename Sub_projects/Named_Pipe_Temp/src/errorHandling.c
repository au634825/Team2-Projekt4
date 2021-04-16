/*
 * errorHandling.c
 *
 *  Created on: 11 Mar 2021
 *      Author: volvofar
 */


#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <limits.h>
#include <fcntl.h>
#include <unistd.h>
#include <syslog.h>
#include "errorHandling.h"
#include "FIFO_queue.h"

#define FIFOMAX 10
extern float queue_array[FIFOMAX];

float errorHandler(float sensorValue, float minThreshold, float maxThreshold) {
	if (sensorValue <= maxThreshold && sensorValue >= minThreshold) {
		int numOfEq = 0;
		for (int i = 0; FIFOMAX > i; i++) {
			if (queue_array[i] == sensorValue) {
				numOfEq++;
			}
		}
		if (numOfEq == FIFOMAX) { // compare them
			syslog(LOG_NOTICE, "Error: Sensor is frozen - value do not change"); // Write to logfile
			return -1;
		} else {
			numOfEq = 0;
			FIFO(sensorValue);
			return sensorValue;
		}
	} else {
		syslog(LOG_NOTICE, "Failed to get temp, Threshold exceeded"); // Write to logfile
		return -1;
	}
	return 0;
}
