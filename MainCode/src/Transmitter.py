import time
from random import randrange
import paho.mqtt.client as mqtt


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
        voltage = 1 + randrange(10)
        current = 1 + randrange(10)
        power = round(voltage * current, 2)
        # Final power from sensor register
        resistance = round(voltage / current, 2)
        irradiance = randrange(1)
        temperature = randrange(100)

        context = [voltage,
                   current,
                   power,
                   resistance,
                   irradiance,
                   temperature]

        print('sending', context)
        client2.publish("Testdevice/team2_module/DATA", str(context))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.username_pw_set(username="team2", password="team2")


client.connect("localhost", 8000, 60)
try:
    client.loop_forever()
    Connected = False
    while not Connected:  # Wait for connection
        time.sleep(0.1)
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()


def getvoltage():
    print("hello")
