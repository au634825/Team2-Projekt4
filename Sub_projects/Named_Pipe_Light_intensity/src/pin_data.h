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

//rød led:
void pwm_mosfet_period(int);
void pwm_mosfet_duty(int);
void pwm_mosfet_enable(int);


#endif /* PIN_DATA_H_ */
