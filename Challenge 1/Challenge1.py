import time
import random
import paho.mqtt.client as paho
from paho import mqtt

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print("Message: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(callback_api_version=paho.CallbackAPIVersion.VERSION1, client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect


client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("mwyeoh123@gmail.com", "Blue8080")
client.connect("9b6f4baa8bcb4748813d9252223d7399.s1.eu.hivemq.cloud", 8883)

client1 = paho.Client(callback_api_version=paho.CallbackAPIVersion.VERSION1, client_id="1", userdata=None, protocol=paho.MQTTv5)
client1.on_connect = on_connect


client1.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client1.username_pw_set("mwyeoh123@gmail.com", "Blue8080")
client1.connect("9b6f4baa8bcb4748813d9252223d7399.s1.eu.hivemq.cloud", 8883)


# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish


# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("encyclopedia/#", qos=1)


# a single publish, this can also be done in loops, etc.



while (1):
  client.loop() 
  client.publish("encyclopedia/temperature", payload=f"{random.randint(0, 10)}", qos=1)
  client1.publish("encyclopedia/wind", payload=f"{random.randint(0, 10)}", qos=1)
  time.sleep(3)
    
