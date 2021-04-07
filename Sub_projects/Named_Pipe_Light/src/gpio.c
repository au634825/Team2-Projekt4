/*
 * gpio.c
 *
 *  Created on: 7 Apr 2021
 *      Author: volvofar
 */

#include <stdio.h>
#include <stdlib.h>
#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <unistd.h>
#include "gpio.h"

void PIN_59(int pin59) {
	FILE *io59_direction = fopen("/sys/class/gpio/gpio59/direction", "w+");
	fprintf(io59_direction, "out"); //setting output
	fclose(io59_direction);

	FILE *io59_value = fopen("/sys/class/gpio/gpio59/value", "w+");
	fprintf(io59_value, "%d\n", pin59);
	fclose(io59_value);
}

void PIN_58(int pin58) {
	FILE *io58_direction = fopen("/sys/class/gpio/gpio58/direction", "w+");
	fprintf(io58_direction, "out"); //setting output
	fclose(io58_direction);

	FILE *io58_value = fopen("/sys/class/gpio/gpio58/value", "w+");
	fprintf(io58_value, "%d\n", pin58);
	fclose(io58_value);
}
