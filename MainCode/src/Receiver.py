from random import randrange
import paho.mqtt.client as mqtt
import IPCHandler as IPC
import json

with open("config.json") as json_data_file:
    config = json.load(json_data_file)


def initIPC():
    try:
        IPC.makefifo(config['pipes']['panelangel'])
        IPC.makefifo(config['pipes']['brightness'])
        IPC.makefifo(config['pipes']['resistanceGET'])
        IPC.makefifo(config['pipes']['resistanceVALUE'])

        IPC.makefifo(config['pipes']['voltage'])
        IPC.makefifo(config['pipes']['current'])
        IPC.makefifo(config['pipes']['power'])
        IPC.makefifo(config['pipes']['irradianceGET'])
        IPC.makefifo(config['pipes']['irradianceVALUE'])
        IPC.makefifo(config['pipes']['temperatureGET'])
        IPC.makefifo(config['pipes']['temperatureVALUE'])

        #setDefaultValues()
        print("Init Done")
    except FileExistsError:
        print("Files already exists.")
        setDefaultValues()
        print("Init Done")
    pass


def setDefaultValues():
    IPC.ipcSend(config['pipes']['panelangel'],
                config['defaultValues']['panelangel'])
    IPC.ipcSend(config['pipes']['brightness'],
                config['defaultValues']['brightness'])
    IPC.ipcSend(config['pipes']['resistance'],
                config['defaultValues']['resistance'])


def decoder():
    print("HEJ")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("Testdevice/team2_module/RECEIVE")


# def on_publish(client, userdata, result):  # create function for callback
#    print("data published \n")
#    pass


# The callback for when a PUBLISH message is received from the server.

def on_message(client2, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    print(type(msg.payload))


initIPC()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# client.on_publish = on_publish
client.username_pw_set(username="team2", password="team2")
#client.connect("localhost", 8000, 60)
client.connect("broker.emqx.io", 1883, 60)
try:
    client.loop_forever()
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
