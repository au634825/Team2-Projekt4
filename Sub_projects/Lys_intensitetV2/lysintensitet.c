#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h>
#include "pin_data.h"

int nul_procent = 0;
int femogtyve_procent = 177500;
int halvtreds_procent = 287500;
int femoghalvfjers_procent = 390000;
int ethundrede_procent = 500000;

/* backup:
int femogtyve_procent = 389706;
int halvtreds_procent = 426471;
int femoghalvfjers_procent = 463235;
int ethundrede_procent = 500000;
*/


int main(){ 
    pwm_rgled_setup();
    pwm_rled_period(500000);
    pwm_rled_duty(0);
    pwm_rled_enable(1); //rød led
    
    
    while(1){
        
        int input; 
   //    printf("Tast '1' for COB LED 1 (kold)\n");
    //   printf("Tast '2' for COB LED 2 (varm)\n");
       printf("Giv input [0, 25, 50, 75, 100]:");
  
       scanf("%d", &input);


        // COB LED 1
        if (input == 1){
            //kode til at enable relæ
            printf("\n>> COB LED '1' er nu valgt!\n");
        }

        // COB LED 2
        if (input == 2){
            //kode til at enable relæ
            printf("\n>> COB LED '2' er nu valgt!\n");
        }


        // 0%
        if (input == 0){
            pwm_rled_duty(nul_procent);
            printf(">> indtastet er: %d duty bliver: %d\n\n"
                               ,input, nul_procent);
        }

        // 25%
        if (input == 25 ){
            pwm_rled_duty(femogtyve_procent); //skal tweakes se beregninger timebox 6
            printf(">> indtastet er: %d duty bliver: %d\n\n"
                         ,input, femogtyve_procent);
        }   
        
        // 50%
        if (input == 50 ){
            pwm_rled_duty(halvtreds_procent); //skal tweakes se beregninger timebox 6
            printf(">> indtastet er: %d duty bliver: %d\n\n"
                         ,input, halvtreds_procent);
        }   
        
        // 75%
        if (input == 75 ){
            pwm_rled_duty(femoghalvfjers_procent); //skal tweakes se beregninger timebox 6
            printf(">> indtastet er: %d duty bliver: %d\n\n"
                    ,input, femoghalvfjers_procent);
        }   
        
        // 100%
        if (input == 100 ){
            pwm_rled_duty(ethundrede_procent);
            printf(">> indtastet er: %d duty bliver: %d\n\n"
                        ,input, ethundrede_procent);
        }   
        

    }
return 0; 
} 

