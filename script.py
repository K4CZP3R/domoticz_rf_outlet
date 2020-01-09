import paho.mqtt.client as mqtt
import json, subprocess, time
import sys, signal
from RfOutlet import RfOutlet
from RfOutletDb import RfOutletDb
from Tools import Tools
from LogicResponse import LogicResponse

repeat_signal_for_s = 20

def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

outlet_1 = RfOutlet("00014056", 1, 0, False)
outlet_2 = RfOutlet("00014057", 2, 0, False)
outlet_3 = RfOutlet("00014058", 3, 0, False)
outlet_db = RfOutletDb([outlet_1, outlet_2, outlet_3])
print(f"There are {outlet_db.count_outlets()} outlets defined!")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("domoticz/out")

def on_message(client, userdata, msg):
    payload_encoded = msg.payload.decode("UTF-8")
    payload_dict = json.loads(payload_encoded)

    switch_id = payload_dict['id']
    switch_state = payload_dict['nvalue']
    switch_name = payload_dict['name']
    print(f"[on_message] Id: {switch_id}")
    print(f"[on_message] State: {switch_state}")
    print(f"[on_message] Name: {switch_name}")

    db_resp = outlet_db.get_outlet_by_dom_id(switch_id)
    if not db_resp.success:
        return
    outlet = db_resp.content
    outlet: RfOutlet

    outlet.executed = False
    outlet.state = switch_state
    outlet.state_changed_at = Tools.get_unix_time()
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)
client.loop_start()


while True:

    for outlet in outlet_db.get_outlets():
        check_time = Tools.get_unix_time()

        outlet: RfOutlet
        if outlet.executed:
            #print(f"[{outlet.dom_id}] is already executed!")
            continue

        if (check_time - outlet.state_changed_at) > repeat_signal_for_s:
            print(f"[{outlet.dom_id}] stopped executing ({repeat_signal_for_s}s timeout)")
            outlet.executed = True
            continue

        print(f"[{outlet.dom_id}] changing {outlet.rf_id} to state {outlet.state}")
        Tools.execute_rf_command(
            outlet.rf_id,
            outlet.state
        )
    
    #time.sleep(1)




        

        