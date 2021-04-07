/*
 * NamedPipeCommunication.c
 *
 *  Created on: 4 Mar 2021
 *      Author: volvofar
 */

#include <stdio.h>
#include <syslog.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include "NamedPipeCommunication.h"
#include "errorHandling.h"

//extern float sensorValue;

int pipeListener(char *path, float (*function)(), char *sensorType,
		float minThreshold, float maxThreshold) {
	// Sensor function send through errorHandler
	float sensorValue = errorHandler(function(), minThreshold, maxThreshold);
	int fd;

	char strGet[80], strSend[80];
	char pathGet[80], pathValue[80];
	strcat(pathGet, path);
	strcat(pathGet, "GET");
	strcat(pathValue, path);
	strcat(pathValue, "VALUE");
	while (1) {
		memset(strGet, 0, sizeof strGet);
		// First open in read only and read
		fd = open(pathGet, O_RDONLY);
		read(fd, strGet, 80);

		// If "GET"
		if (strncmp("GET", strGet, 3) == 0) {
			close(fd);
			// Now open in write mode and write
			// string taken from transmitter.
			fd = open(pathValue, O_WRONLY);
			gcvt(sensorValue, 5, strSend);
			write(fd, strSend, strlen(strSend) + 1);
			close(fd);
			sleep(2);
		} else {
			// If not "GET" error message
			syslog(LOG_NOTICE, "Wrong request message for %s pipe", sensorType);
			continue;
		}
	}
	return 0;
}

//int pipeListener(char *path, float (*function)(), char *sensorType,
//		float minThreshold, float maxThreshold) {
//	// Sensor function send through errorHandler
//	float sensorValue = errorHandler(function(), minThreshold, maxThreshold);
//	int fd;
//
//	// FIFO file path
//	char *myfifo = path;
//
//	// Creating the named file(FIFO)
//	// mkfifo(<pathname>,<permission>)
//	mkfifo(myfifo, 0666);
//
//	char strGet[80], strSend[80];
//	while (1) {
//		// First open in read only and read
//		fd = open(myfifo, O_RDONLY);
//		read(fd, strGet, 80);
//
//		// If "GET"
//		if (strncmp("GET", strGet, 3) == 0) {
//			close(fd);
//			// Now open in write mode and write
//			// string taken from transmitter.
//			fd = open(myfifo, O_WRONLY);
//			gcvt(sensorValue, 5, strSend);
//			write(fd, strSend, strlen(strSend) + 1);
//			close(fd);
//		} else {
//			// If not "GET" error message
//			syslog(LOG_NOTICE, "Wrong request message for %s pipe", sensorType);
//			continue;
//		}
//	}
//	return 0;
//}
//
