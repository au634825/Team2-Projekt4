/*
 ============================================================================
 Name        : Named_Pipe_Light_intensity.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>
#include <syslog.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include "lysintensitet.h"
#include "pin_data.h"
#include "setitimer.h"

const char path[] = "/tmp/brightness";

int main() {
	// Temperature sensor
	int fd;
	char strGet[80];
	char *EHand;
	const int sec = 30;
	pwm_mosfet_setup();

	while (1) {
		memset(strGet, 0, sizeof strGet);
		// First open in read only and read
		fd = open(path, O_RDONLY);
		read(fd, strGet, 80);
		close(fd);
		int input = (int) strtol(strGet, &EHand, 10);
		timeInterval(sec);
		syslog(LOG_NOTICE, "\nSetitimer starts\n");
		lightIntensity(input);
		syslog(LOG_NOTICE, "\nInput received: %d \n", input);


		sleep(2);
	}
	return 0;
}
