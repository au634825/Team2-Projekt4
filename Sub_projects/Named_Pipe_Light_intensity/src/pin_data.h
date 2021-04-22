/*
 * pin_data.h
 *
 *  Created on: 11 Apr 2021
 *      Author: volvofar
 */

#ifndef PIN_DATA_H_
#define PIN_DATA_H_


///PWM- rød led
void pwm_mosfet_setup();
void gpio_mosfet_fan_direction();

//rød led:
void pwm_mosfet_period(int);
void pwm_mosfet_duty(int);
void pwm_mosfet_enable(int);
void gpio_mosfet_fan_ON();
void gpio_mosfet_fan_OFF();


#endif /* PIN_DATA_H_ */
