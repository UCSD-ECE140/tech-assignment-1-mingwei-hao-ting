import time
import random
import paho.mqtt.client as paho
from paho import mqtt

lobby_name = "mylobby"
team_name = "myteam"
player_name = "player"
moves = {"r" : "RIGHT", "l" : "LEFT", "u" : "UP", "d" : "DOWN"}

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
    global currentTurn
    print("Message: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    
client = paho.Client(callback_api_version=paho.CallbackAPIVersion.VERSION1, client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("mwyeoh123@gmail.com", "Blue8080")
client.connect("9b6f4baa8bcb4748813d9252223d7399.s1.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to game info
client.subscribe("games/mylobby/lobby", qos=1)

client.publish("new_game", payload=f'{{"lobby_name": "{lobby_name}", "team_name": "{team_name}", "player_name": "{player_name}"}}', qos=1)
client.subscribe(f"games/{lobby_name}/{player_name}/game_state", qos=1)

input("Press any key to start the game!")
client.publish(f"games/{lobby_name}/start", payload="START", qos=1)

while (1):
  for i in range(5):
    client.loop() 
    time.sleep(0.1)
  move = input("Which way do you want to move?")
  client.publish(f"games/{lobby_name}/{player_name}/move", payload= moves[move], qos=1)
    
