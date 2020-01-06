import paho.mqtt.client as mqtt
import json, subprocess

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("domoticz/out")

def on_message(client, userdata, msg):
    payload_encoded = msg.payload.decode("UTF-8")
    payload_dict = json.loads(payload_encoded)

    switch_id = payload_dict['id']
    switch_state = payload_dict['nvalue']
    switch_name = payload_dict['name']
    print(f"Id: {switch_id}")
    print(f"State: {switch_state}")
    print(f"Name: {switch_name}")

    if switch_id in outlet_db:
        res = subprocess.Popen(["./kspRfTool", outlet_db[switch_id]['rf_id'], str(switch_state)])
    

    
        
outlet_db = {
    '00000000': {
        'rf_id': '1'
    },
    '00000000': {
        'rf_id': '2'
    },
    '00000000': {
        'rf_id': '3'
    }
}



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)
client.loop_forever()