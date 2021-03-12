#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h>
#include "pin_data.h"

int state = 0;

void button(){
    value();                   //tjek for knaptryk |
    if (value_int == 1){       //knap = HIGH       |
        usleep(70000);         //vent 70ms         |--- Debouncing af knap
        value();               //tjek for knaptryk |
        if (value_int == 1){   //knap = HIGH       |
            usleep(70000);     //vent 70ms         |
            state=(state+1);   //ved knaptryk incrementeres state med 1
            printf( "state nr: %d \n",state); 
        }
    }
} 


int main(){ 
    pin_115_setup(); //knap
    pwm_rgled_setup();
    pwm_rled_period(500000);
    pwm_rled_duty(0);
    pwm_rled_enable(1); //rød led
    
    while(1){
        button();

        // 25%
        if (state == 1 ){
            pwm_rled_duty(389706); //skal tweakes se beregninger timebox 6
            button();
        }   
        
        // 50%
        if (state == 2 ){
            pwm_rled_duty(426471); //skal tweakes se beregninger timebox 6
            button();
        }   
        
        // 75%
        if (state == 3 ){
            pwm_rled_duty(463235); //skal tweakes se beregninger timebox 6
            button();
        }   
        
        // 100%
        if (state == 4 ){
            pwm_rled_duty(500000);
            button();
        }   
        
        // 0%
        else if (state >4){
            pwm_rled_duty(0);
            state = 0;
        }
    }
return 0; 
} 

