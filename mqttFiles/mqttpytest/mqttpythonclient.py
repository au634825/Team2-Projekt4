import paho.mqtt.client as mqtt #import the client1

def on_message(client,userdata,msg):
    print("Message topic: ",msg.topic, " Payload: ",str(msg.payload))

broker_address="mqtt.eclipse.org" 
#broker_address="iot.eclipse.org" #use external broker

print("creating newinstance")
client = mqtt.Client("JenaxCentos8") #create new instance
client.on_message=on_message

print("connecting to broker")
client.connect(broker_address) #connect to broker

print("subscribing to topic","team2/servo_pos")
client.subscribe("team2/servo_pos")

print("Publishing message to topic","team2/servo_pos")
client.publish("team2/servo_pos","90")#publish

client.loop_forever()
