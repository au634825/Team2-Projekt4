import json
import time
import board
import busio
import adafruit_ina260
import sys

sys.path.append('../')
import IPCHandler as IPC

i2c = busio.I2C(board.SCL, board.SDA)
ina260 = adafruit_ina260.INA260(i2c)
print("i2c detected")

with open("../../config.json") as json_data_file:
    config = json.load(json_data_file)

while True:

    voltageGet = IPC.ipcRead1(config['pipes']['multiGET'])
    if voltageGet:
        values = [ina260.voltage,
                  ina260.current,
                  ina260.power]
        IPC.ipcSend(config['pipes']['multiGET'], values)
    time.sleep(1)
