/*
 * NamedPipeCommunication.c
 *
 *  Created on: 4 Mar 2021
 *      Author: volvofar
 */

#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include "NamedPipeCommunication.h"

extern float sensorValue;

int pipeListener(char *path) {
	int fd;

	// FIFO file path
	char *myfifo = path;

	// Creating the named file(FIFO)
	// mkfifo(<pathname>,<permission>)
	mkfifo(myfifo, 0666);

	char str1[80], str2[80];
	while (1) {
		// First open in read only and read
		fd = open(myfifo, O_RDONLY);
		read(fd, str1, 80);

		if (strcmp("GET_VALUE", str1) == 0) {
			close(fd);
			// Now open in write mode and write
			// string taken from user.
			fd = open(myfifo, O_WRONLY);
			gcvt(sensorValue, 5, str2);
			write(fd, str2, strlen(str2) + 1);
			close(fd);
		}
	}
	return 0;
}
