/*
 * pin_data.c
 *
 *  Created on: 11 Apr 2021
 *      Author: volvofar
 */


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "pin_data.h"


///PWM - setup
void pwm_mosfet_setup(){
    FILE* pwm_mosfet_state = fopen("/sys/devices/platform/ocp/ocp:P1_36_pinmux/state", "w+");
    fprintf(pwm_mosfet_state, "pwm"); //sæt pin til at være pwm
	fclose(pwm_mosfet_state);
}

//PWM - settings:
void pwm_mosfet_period(int period_mosfet_val){
    FILE* pwm_io110_period = fopen("/sys/class/pwm/pwmchip0/pwm-0:0/period", "w+");
    fprintf(pwm_io110_period, "%d\n", period_mosfet_val); //send værdier til perioden
    fclose(pwm_io110_period);
}
void pwm_mosfet_duty(int duty_mosfet_val){
    FILE* pwm_io110_duty = fopen("/sys/class/pwm/pwmchip0/pwm-0:0/duty_cycle", "w+");
    fprintf(pwm_io110_duty, "%d\n", duty_mosfet_val); //send værdier til duty_cycle
    fclose(pwm_io110_duty);
}
void pwm_mosfet_enable(int enable_mosfet_val){
    FILE* pwm_io110_enable = fopen("/sys/class/pwm/pwmchip0/pwm-0:0/enable", "w+");
    fprintf(pwm_io110_enable, "%d\n", enable_mosfet_val); //send værdier til duty_cycle
    fclose(pwm_io110_enable);
}
