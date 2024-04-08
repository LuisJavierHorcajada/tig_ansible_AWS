#!/bin/python3

from paho.mqtt import client as mqtt_client
import time
from math import sin

broker = 'ec2-3-81-115-170.compute-1.amazonaws.com'
port = 2883
topic = "service/ansible/asdf"
client_id = f'python-mqtt-001'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    while True:
        msg = f"test,tag1=1,tag2=2 value={sin(msg_count/10)}"
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        time.sleep(0.1)

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
