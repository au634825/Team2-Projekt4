/*
 * sig_handler.c
 *
 *  Created on: 4 Feb 2021
 *      Author: volvofar
 */

#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <syslog.h>
#include <pthread.h>
#include <string.h>
#include "sig_handler.h"
#include "lysintensitet.h"
#include "setitimer.h"
#include "pin_data.h"

void sig_handler(int signo) {
	int nul_procent = 0;
	// Temp update signal
	if (signo == SIGALRM) {
		lightIntensity(nul_procent);
		syslog(LOG_NOTICE, "Light intensity turned off\n");
		gpio_mosfet_fan_OFF();
		syslog(LOG_NOTICE, "Fan turned off\n");
		timeInterval(nul_procent);
		syslog(LOG_NOTICE, "Timer stopped\n");

	}
	else
	{
		syslog(LOG_NOTICE, "gets unknown signal\n");
	}
}
