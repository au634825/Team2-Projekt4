/*
 * setitimer.c
 *
 *  Created on: 16 Feb 2021
 *      Author: volvofar
 */

/*
 * setitimer.c - simple use of the interval timer
 */

#include <sys/time.h>	/* for setitimer */
#include <unistd.h>		/* for pause */
#include <signal.h>		/* for signal */
#include <syslog.h>
#include "sig_handler.h"
#include "setitimer.h"

void timeInterval(int sec) {

	struct itimerval it_val;

	if (signal(SIGALRM, sig_handler) == SIG_ERR) {
		syslog(LOG_NOTICE, "\nCan't call SIGALRM\n");
	}

	it_val.it_interval.tv_sec = sec; /* seconds */
	it_val.it_interval.tv_usec = 0; /* microseconds */
	it_val.it_value = it_val.it_interval;

	// setup setitimer clock
	if (setitimer(ITIMER_REAL, &it_val, NULL) == -1) {
		syslog(LOG_NOTICE, "\nCan't run setitimer\n");
	}
}

//int setitimer(ITIMER_REAL, it_interval, timeval);

//if (setitimer(ITIMER_REAL, &it_val, NULL) == -1) {
//	syslog(LOG_NOTICE, "Fault at setitimer");
//	exit(1);
//}
