from random import randrange
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_publish(client, userdata, result):  # create function for callback
    print("data published \n")
    pass


# The callback for when a PUBLISH message is received from the server.
def on_message(client2, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.username_pw_set(username="team2", password="team2")
client.connect("localhost", 8000, 60)
client.subscribe("Testdevice/team2_module/panelangle")

try:
    client.loop_forever()
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
