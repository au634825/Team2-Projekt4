import time
import board
import busio
import adafruit_ina260
import IPCHandler as IPC
i2c = busio.I2C(board.SCL, board.SDA)
ina260 = adafruit_ina260.INA260(i2c)
print("i2c detected")

while True:

    voltageGet = IPC.ipcRead1("/tmp/voltageGET")
    if voltageGet:
        IPC.ipcSend("/tmp/voltageVALUE", ina260.voltage)

    currentGet = IPC.ipcRead1("/tmp/voltageGET")
    if voltageGet:
        IPC.ipcSend("/tmp/voltageVALUE", ina260.voltage)

    print("Current:", ina260.current)
    print("Voltage:", ina260.voltage)
    print("Power:", ina260.power)

    time.sleep(1)

