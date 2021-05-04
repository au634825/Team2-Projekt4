/*
 * LUXSensor.c
 *
 *  Created on: 7 Apr 2021
 *      Author: volvofar
 */

#include <stdio.h>
#include <syslog.h>
#include <stdlib.h>
#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <unistd.h>
#include "gpio.h"

float lightSensor() {

	//while løkken køre uendeligt da der ikke er sat noget stop
	while (1) {

		//navn til at holde en integer værdi
		int file;

		//char med navnet bus til at holde stien til i2c modulet
		char *bus = "/dev/i2c-2"; //i2c-1 da vi køre på i2c modul 1

		//O_RDWR betyder "open read and write" i denne if betingese tjekker vi om
		//intergeren "file" er ligmed 1 eller 0, altså om den er true eller false
		//hvis det kan lade sig gøre at åbne bussen der peger på stien "/dev/i2c-1"
		//i read and write mode så kommer der til at stå
		//if (1 =< 0) og så køre betingelsen ikke (FALSE)
		//hvis det derimod ikke er muligt at åbne stien, så er det fordi sensoren
		//ikke er tilkoblet eller konfigureret ukorekt og så kommer der til at stå:
		//if (0 =< 0) her køre betingelsen og printer "Bus kunne ikke åbnes" og
		//stopper derefter eksekveringen af programmet med exit(1);

		if ((file = open(bus, O_RDWR)) < 0) {
			syslog(LOG_NOTICE, "Bus kunne ikke åbnes. \n");
			exit(1);
		}

		//når man køre "sudo i2cdetect -r 2" får man en tabel med alle de
		//hexidecimale adresser på i2c-1 modulet, her aflæses det at når sensoren
		//monteres får jeg adressen 0x39
		////Get I2C device, TSL2561 I2C address is 0x39(57)

		//ioctl er et control device som tager file (altså stien til bussen)
		//og sætter adressen til det modul vi gerne vil tilgå.

		ioctl(file, I2C_SLAVE, 0x39);

		//ifølge databladet til TSL2561 LUX-lyssensor modulet er der nogle
		//konfigurationer som først skal sættes op før vi kan måle data fra det.

		// det første

		// Select control register opsættes til at (0x00 | 0x80)
		// Power ON mode(0x03)
		char config[2] = { 0 };
		config[0] = 0x80;
		config[1] = 0x03;
		write(file, config, 2);

		// Select timing register(0x01 | 0x80)
		// Nominal integration time = 402ms(0x02)
		config[0] = 0x81;
		config[1] = 0x02;
		write(file, config, 2);

		// Læs 2 bytes data fra register(0x0C | 0x80)
		char reg[1] = { 0x8C };
		write(file, reg, 1);
		char data[2] = { 0 };
		read(file, data, 2);

		if (read(file, data, 2) != 2) {
			syslog(LOG_NOTICE, "Error i input/output\n");
		}

		else {
			//Konverter dataen
			//der opsættes en kalibreringsfaktor for at få ens data som med
			float irradiance;
			float calib = 3.2;
			float messureLUX = (data[1] * 256 + data[0]) / calib;

			if(messureLUX > 300)
			{
				irradiance = 0.0109 * (messureLUX * 1.449) + 96.475;
			}
			else
			{
				irradiance = 0;
			}

			return irradiance;
		}
	}
	return 0;
}



//printf("The lux value is -> %.2f lux \n", messure);
//syslog(LOG_NOTICE, "sensorValue %0.1f \n", messureLUX);

//usleep(500000);
