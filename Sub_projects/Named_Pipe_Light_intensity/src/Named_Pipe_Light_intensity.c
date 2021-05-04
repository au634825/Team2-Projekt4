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
	const int sec = 15;
	//pwm_mosfet_export();
	pwm_mosfet_setup();
	gpio_mosfet_fan_direction();


	while (1) {
		memset(strGet, 0, sizeof strGet);
		// First open in read only and read
		fd = open(path, O_RDONLY);
		if (!fd) {
			syslog(LOG_NOTICE, "Error, could not open file\n");
		}
		read(fd, strGet, 80);
		close(fd);
		int input = (int) strtol(strGet, &EHand, 10);
		timeInterval(sec);
		syslog(LOG_NOTICE, "\nSetitimer starts\n");
		gpio_mosfet_fan_ON();
		syslog(LOG_NOTICE, "Fan turned on\n");
		lightIntensity(input);
		syslog(LOG_NOTICE, "\nInput received: %d \n", input);

		sleep(2);
	}
	return 0;
}
