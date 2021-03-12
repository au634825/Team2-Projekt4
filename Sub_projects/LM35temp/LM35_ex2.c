//standard biblioteker
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h>

int main(){
    /*char til at holde de rå data eftersom de obevares i ascii tegn
    og kan derfor ikke læses ind som integers med det samme */
    char value_str[5];
    
    //integer til at holde heltallet når det konverteres fra char
    int value_int = 0;
    
    //integer til at holde heltallet efter beregningen tilk grader
    int test;

    //stien til AIN0 (P1_19) åbnes til "read mode"
    FILE* f0 = fopen("/sys/bus/iio/devices/iio:device0/in_voltage0_raw", "r");

    while(1){
        fread(&value_str, 5, 5, f0);
            
        value_int = strtol(value_str,NULL,0);
            
        //konvertering af raw data til grader
        test=(value_int*1800/4096)/10; 
            
        //print til konsollen
        printf("%i\n", test);
            
        //lukker filen og flusher bufferen
        fflush(stdout); 
        //pause i 0,5sec
        usleep(500000);
        //vender tilbage til begyndelsen af filen "f0"
        //så der kan tages nye målinger
        rewind(f0);
    }
}

