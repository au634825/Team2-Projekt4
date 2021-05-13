import time

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        global Connected
        Connected = True
        print("Connected with result code " + str(rc))
    else:
        print("Connected failed with result code " + str(rc))


def on_publish(client, userdata, result):  # create function for callback
    print("data published \n")
    client.disconnect()
    pass


def on_disconnect(client, userdata, rc):
    print("client disconnected ok")


client = mqtt.Client()
client.on_connect = on_connect
# client.on_publish = on_publish
client.username_pw_set(username="team2", password="team2")
client.connect("localhost", 8000, 60)
print("Connecting...")
#client.connect("test.mosquitto.org", 1883, 60)
client.loop_start()
global Connected
Connected = False
while not Connected:  # Wait for connection
    time.sleep(0.1)
ret = client.publish("Testdevice/team2_module/DATA", "test-publishing")
time.sleep(3)
