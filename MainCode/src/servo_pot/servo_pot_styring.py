# PRO4 - Servo styring til loadmodstand (RDS3115MG 270deg servo)
import json
import time
import sys
import Adafruit_BBIO.PWM as PWM

sys.path.append('./MainCode/src/')
import IPCHandler as IPC

with open("./MainCode/config.json") as json_data_file:
    config = json.load(json_data_file)

servo_pin = "P8_13"
duty_min = 3
duty_max = 15.3
duty_span = duty_max - duty_min

PWM.start(servo_pin, (100 - duty_min), 60.0, 1)  # start position

max_ohm_const = 924  # ohm målt manuelt
min_deg_const = 28.3477045  # 105 minimum ohm = 28.3477045 grader
max_deg_const = 257.55779  # 884.5 maximim ohm = 257.55779 grader
buffer_const = 1  # buffer degree (tolerence)
duty_scale_const = 94  # duty værdi på 94 svare til 100ohm

while True:
    #ohminput = float(input("Indtast modstands-værdi imellem 0 og 924: "))
    ohminput = float(IPC.ipcRead1(config['pipes']['resistance']))

    angle2 = (((ohminput - buffer_const) / (max_ohm_const / (max_deg_const - min_deg_const))) + min_deg_const)

    # til justering 1.:
    # angle3=max_ohm_const/270
    # print("vinkel (debug) %",angle3)

    if ohminput < 70:  # til små modstandsværdier under 70ohm
        PWM.set_duty_cycle(servo_pin, duty_scale_const)
        time.sleep(0.5)

    if ohminput == 'x':  # stopper servomotor ved "x" input
        PWM.stop(servo_pin)
        PWM.cleanup()
        break

    angle_f = float(angle2)
    # konverter fra ohm til vinkel
    duty = 100 - ((angle_f / 270) * duty_span + duty_min)

    # til justering 2.:
    # print("duty værdi (debug) %",duty)

    # sætter endelig vinkel der svare til indtastet modstandsværdi:
    PWM.set_duty_cycle(servo_pin, duty)

##BEMÆRK!------
# max_ohm_const: finde én gang ved at måle manuelt på pot

# debug justering 1.:
# min_deg_const: for at finde minimums vinklen skal "angle3" printes til terminalen
# angiv nu en højere og højere modstand på inputtet indtil
# multimeteret lige akurat viser over 0ohm. når dette er
# tilfældet skrives angle3 værdien ind i min_deg_const

# debug justering 1.:
# max_deg_const: for at finde minimums vinklen skal "angle3" printes til terminalen
# angiv nu en højere og højere modstand på inputtet indtil
# multimeteret lige akurat viser 924. når dette er
# tilfældet skrives angle3 værdien ind i max_deg_const

# buffer_const:  justeres til sidst så de små ohm værdier passer bedst med
# det indtastede typisk imellem 1 og 3.

# debug justering 2.:
# duty_scale_const: #når modstandsværdier er små (under 70ohm) og man evt. vil
# gå fra 5 ohm til 10 så er det svært at ramme præcist
# vi drejer derfor servoen op til en højere modstand først
# og derefter ned til den mindre igen for at den indstiller
# sig korrekt. aktiver "justering 2." for at finde værdien
