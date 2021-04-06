#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h>

char value_str[2];
int value_int = 0;

void pin_115_setup(){
    FILE* io115_state = fopen("/sys/devices/platform/ocp/ocp:P2_34_pinmux/state", "w+"); 
    fprintf(io115_state, "gpio_input"); //sæt gpiostate til input
	fclose(io115_state);
}
void value(){
    FILE* io115_value = fopen("/sys/class/gpio/gpio115/value", "r+"); 
    fread(&value_str, 5, 5, io115_value);//læs data ved knaptryk
	value_int = strtol(value_str,NULL,0);
    fclose(io115_value);
}


///PWM- rød led
void pwm_rgled_setup(){
    FILE* pwm_rled_state = fopen("/sys/devices/platform/ocp/ocp:P1_36_pinmux/state", "w+"); 
    fprintf(pwm_rled_state, "pwm"); //sæt pin til at være pwm
	fclose(pwm_rled_state);    
}

//rød led:
void pwm_rled_period(int period_rled_val){
    FILE* pwm_io110_period = fopen("/sys/class/pwm/pwmchip0/pwm-0:0/period", "w+"); 
    fprintf(pwm_io110_period, "%d\n", period_rled_val); //send værdier til perioden
    fclose(pwm_io110_period);
}
void pwm_rled_duty(int duty_rled_val){ 
    FILE* pwm_io110_duty = fopen("/sys/class/pwm/pwmchip0/pwm-0:0/duty_cycle", "w+"); 
    fprintf(pwm_io110_duty, "%d\n", duty_rled_val); //send værdier til duty_cycle
    fclose(pwm_io110_duty);    
}
void pwm_rled_enable(int enable_rled_val){ 
    FILE* pwm_io110_enable = fopen("/sys/class/pwm/pwmchip0/pwm-0:0/enable", "w+"); 
    fprintf(pwm_io110_enable, "%d\n", enable_rled_val); //send værdier til duty_cycle
    fclose(pwm_io110_enable);    
}

