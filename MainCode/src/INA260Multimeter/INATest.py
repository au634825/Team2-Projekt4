import time
import ast
import board
import busio
import adafruit_ina260
i2c = busio.I2C(board.SCL, board.SDA)
ina260 = adafruit_ina260.INA260(i2c)

while True:
    print("i2c detected")
    print("Current:", ina260.current)
    print("Voltage:", ina260.voltage)
    print("Power:", ina260.power)
    
    multi = [ina260.current, ina260.voltage, ina260.power]
    print(multi)
    
    multi = str(multi)
    print(type(multi))
    multi = eval(multi)

    print(multi)
    print(type(multi))
    
    voltage = multi[0]
    current = multi[1]
    power = multi[2]
    print(voltage)
    print(current)
    print(power)

    time.sleep(1)
