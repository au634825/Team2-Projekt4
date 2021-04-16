import json
import time
from random import randrange
import paho.mqtt.client as mqtt
import IPCHandler as IPC

with open("../config.json") as json_data_file:
    config = json.load(json_data_file)


def on_connect(client, userdata, flags, rc):
    global Connected
    Connected = True
    print("Connected with result code " + str(rc))
    client.subscribe("Testdevice/team2_module/REQUEST")


def on_publish(client, userdata, result):  # create function for callback
    print("data published \n")
    pass


# The callback for when a PUBLISH message is received from the server.
def on_message(client2, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if msg.payload == b'SEND_DATA':
        context = SensorValues()
        # context = [1, 2, 3, 4, 5, 6]
        print('sending', context)
        client2.publish("Testdevice/team2_module/DATA", str(context))


def SensorValues():
    print("Getting sensor values...")
    IPC.ipcSend(config['pipes']['temperatureGET'], "GET")
    temperature = IPC.ipcRead1(config['pipes']['temperatureVALUE'])
    print(type(temperature))
    temperature = eval(str(temperature))
    print(type(temperature))
    print("temperature is :  " + temperature)
    print("Got temperature: " + str(temperature))

    IPC.ipcSend(config['pipes']['irradianceGET'], "GET")
    irradiance = IPC.ipcRead1(config['pipes']['irradianceVALUE'])
    irradiance = int(eval(irradiance))
    print("Got irradiance: " + str(irradiance))

    IPC.ipcSend(config['pipes']['multiGET'], "GET")
    multi = IPC.ipcRead1(config['pipes']['multiVALUE'])
    multi = eval(multi)
    voltage = (multi[0] / +0.001) / 1000
    current = multi[1] + 0.001
    power = multi[2]
    print("Got voltage: " + str(voltage))
    print("Got current: " + str(current))
    print("Got power: " + str(power))

    resistance = float(voltage) / float(current)

    decimals = 1
    context = [round(voltage, decimals),
               round(current, decimals),
               round(power, decimals),
               round(resistance, decimals),
               irradiance,
               round(temperature, 1)]
    return context


def getSensorValuesOr():
    print("Getting sensor values...")
    IPC.ipcSend(config['pipes']['irradiance'], "GET")
    irradiance = IPC.ipcRead(config['pipes']['irradiance'])
    print("Got irradiance: " + str(irradiance))

    IPC.ipcSend(config['pipes']['voltage'], "GET")
    voltage = IPC.ipcRead(config['pipes']['voltage'])
    print("Got voltage: " + str(voltage))

    IPC.ipcSend(config['pipes']['current'], "GET")
    current = IPC.ipcRead(config['pipes']['current'])
    print("Got current: " + str(current))

    IPC.ipcSend(config['pipes']['power'], "GET")
    power = IPC.ipcRead(config['pipes']['power'])
    print("Got power: " + str(power))

    IPC.ipcSend(config['pipes']['temperature'], "GET")
    temperature = IPC.ipcRead(config['pipes']['temperature'])
    print("Got temperature: " + str(temperature))

    print("Done reading for sensors")
    resistance = float(voltage) / float(current)

    context = [voltage,
               current,
               power,
               resistance,
               irradiance,
               temperature]
    return context


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.username_pw_set(username="team2", password="team2")

# client.connect("localhost", 8000, 60)
client.connect("broker.emqx.io", 1883, 60)
try:
    client.loop_forever()
    Connected = False
    while not Connected:  # Wait for connection
        time.sleep(0.1)
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
