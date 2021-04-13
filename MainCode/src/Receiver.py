import time
from random import randrange
import paho.mqtt.client as mqtt
import IPCHandler as IPC
import json

from MainCode.src import Timer

with open("../config.json") as json_data_file:
    config = json.load(json_data_file)

timer = Timer.Timer(20)


def initIPC():
    try:
        IPC.makefifo(config['pipes']['panelangel'])
        IPC.makefifo(config['pipes']['brightness'])
        IPC.makefifo(config['pipes']['resistance'])

        IPC.makefifo(config['pipes']['multiGET'])
        IPC.makefifo(config['pipes']['multiVALUE'])
        IPC.makefifo(config['pipes']['irradianceGET'])
        IPC.makefifo(config['pipes']['irradianceVALUE'])
        IPC.makefifo(config['pipes']['temperatureGET'])
        IPC.makefifo(config['pipes']['temperatureVALUE'])

        # setDefaultValues()
        print("Init Done")
    except FileExistsError:
        print("Files already exists.")
        # setDefaultValues()
        print("Init Done")
    pass


def setDefaultValues():
    IPC.ipcSend(config['pipes']['panelangel'],
                config['defaultValues']['panelangel'])
    IPC.ipcSend(config['pipes']['brightness'],
                config['defaultValues']['brightness'])
    IPC.ipcSend(config['pipes']['resistance'],
                config['defaultValues']['resistance'])


def decoder(inputBytes):
    values = eval(inputBytes)
    return values


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("Testdevice/team2_module/RECEIVE")


# def on_publish(client, userdata, result):  # create function for callback
#    print("data published \n")
#    pass
# The callback for when a PUBLISH message is received from the server.

def on_message(client2, userdata, msg):
    timer.startTimer()
    print(str(msg.payload))
    print(type(msg.payload))
    inputValues = decoder(msg.payload)
    IPC.ipcSend(config['pipes']['panelangel'], inputValues[2])
    IPC.ipcSend(config['pipes']['brightness'], inputValues[3])
    res = [int(i) for i in inputValues.split() if i.isdigit()]
    IPC.ipcSend(config['pipes']['resistance'], str(res[0]))


initIPC()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# client.on_publish = on_publish
client.username_pw_set(username="team2", password="team2")
# client.connect("localhost", 8000, 60)
client.connect("broker.emqx.io", 1883, 60)
try:
    client.loop_start()
    while True:
        if timer.isActive():
            if timer.isTimeElapsed():
                timer.stopTimer()
                setDefaultValues()

        time.sleep(1)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
