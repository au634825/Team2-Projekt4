/*
 * pin_data.c
 *
 *  Created on: 11 Apr 2021
 *      Author: volvofar
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <syslog.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include "pin_data.h"

///PWM - setup
void pwm_mosfet_setup() {
	FILE *pwm_mosfet_state = fopen(
			"/sys/devices/platform/ocp/ocp:P9_21_pinmux/state", "w+");
	fprintf(pwm_mosfet_state, "pwm"); //sæt pin til at være pwm
	fclose(pwm_mosfet_state);
}
void gpio_mosfet_fan_direction() {
	// Allocates a buffer array and value buffer
	char buffer[5];
	FILE *gpio_fan_state = fopen("/sys/class/gpio/gpio60/direction", "w+");
	if (!gpio_fan_state) {
		printf("Error, could not open file\n");
	}
	strcpy(buffer, "out");
	fwrite(&buffer, sizeof(char), 3, gpio_fan_state);
	fclose(gpio_fan_state);

	FILE *gpio_fan_pin = fopen("/sys/class/gpio/gpio60/value", "w");
	if (!gpio_fan_pin) {
		syslog(LOG_NOTICE, "Error, could not open file\n");
	}
	fprintf(gpio_fan_pin, "%d", 0);
	fclose(gpio_fan_pin);
}

//PWM - settings:
void pwm_mosfet_period(int period_mosfet_val) {
//	FILE *pwm_io110_period = fopen("/sys/class/pwm/pwmchip0/pwm-0:0/period",
//			"w+");
	FILE *pwm_io110_period = fopen("/sys/devices/platform/ocp/48300000.epwmss/48300200.pwm/pwm/pwmchip1/pwm-1:1/period",
			"w+");
	if (!pwm_io110_period) {
					syslog(LOG_NOTICE, "Error, could not open period file\n");
	}
	fprintf(pwm_io110_period, "%d\n", period_mosfet_val); //send værdier til perioden
	fclose(pwm_io110_period);
}
void pwm_mosfet_duty(int duty_mosfet_val) {
//	FILE *pwm_io110_duty = fopen("/sys/class/pwm/pwmchip0/pwm-0:0/duty_cycle",
//			"w+");
	FILE *pwm_io110_duty = fopen("/sys/devices/platform/ocp/48300000.epwmss/48300200.pwm/pwm/pwmchip1/pwm-1:1/duty_cycle",
			"w+");
	if (!pwm_io110_duty) {
				syslog(LOG_NOTICE, "Error, could not open duty file\n");
	}
	fprintf(pwm_io110_duty, "%d\n", duty_mosfet_val); //send værdier til duty_cycle
	fclose(pwm_io110_duty);
}
void pwm_mosfet_enable(int enable_mosfet_val) {
//	FILE *pwm_io110_enable = fopen("/sys/class/pwm/pwmchip0/pwm-0:0/enable",
//			"w+");
	FILE *pwm_io110_enable = fopen("/sys/devices/platform/ocp/48300000.epwmss/48300200.pwm/pwm/pwmchip1/pwm-1:1/enable",
			"w+");
	if (!pwm_io110_enable) {
			syslog(LOG_NOTICE, "Error, could not open enable file\n");
	}
	fprintf(pwm_io110_enable, "%d\n", enable_mosfet_val); //send værdier til duty_cycle
	fclose(pwm_io110_enable);
}

void gpio_mosfet_fan_ON() {
	FILE *gpio_fan_pin = fopen("/sys/class/gpio/gpio60/value", "w");
	if (!gpio_fan_pin) {
		syslog(LOG_NOTICE, "Error, could not open file\n");
	}
	fprintf(gpio_fan_pin, "%d", 1);
	fclose(gpio_fan_pin);
}

void gpio_mosfet_fan_OFF() {
	FILE *gpio_fan_pin = fopen("/sys/class/gpio/gpio60/value", "w");
	if (!gpio_fan_pin) {
		syslog(LOG_NOTICE, "Error, could not open file\n");
	}
	fprintf(gpio_fan_pin, "%d", 0);
	fclose(gpio_fan_pin);
}
