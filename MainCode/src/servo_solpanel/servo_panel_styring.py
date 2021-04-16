import json

import Adafruit_BBIO.PWM as PWM
import sys

sys.path.append('../')
import IPCHandler as IPC

with open("../../config.json") as json_data_file:
    config = json.load(json_data_file)




servo_pin = "P9_21"

duty_min = 8
duty_max = 14.5
duty_span = duty_max - duty_min

PWM.start(servo_pin, (100 - duty_min), 65.0, 1)

while True:
    angle = input("Angle (0 to 180 x to exit):")
    #angle = IPC.ipcRead1(config['pipes']['panelangel'])
    if angle == 'x':
        PWM.stop(servo_pin)
        PWM.cleanup()
        break

    angle_f = float(angle)
    duty = 100 - ((angle_f / 90) * duty_span + duty_min)
    PWM.set_duty_cycle(servo_pin, duty)
