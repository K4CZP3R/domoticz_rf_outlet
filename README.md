# Control RF outlet using Domoticz via MQTT

**Project name:** `domoticz_rf_outlet`

To this to work you will need to compile `kspRfOutlet.cpp`.  
To compile it you will need: `wiringPi` and `RaspberryNewRemoteSwitch` (Guide available [here](https://github.com/K4CZP3R/RaspberryNewRemoteSwitch))

## How to compile `kspRfOutlet.cpp`
1. After you have cloned `RaspberryNewRemoteSwitch` and installed `wiringPi`, save the path to `RaspberryNewRemoteSwitch` you will need it to compile this file.  
(*Example*: `/home/pi/RaspberryNewRemoteSwitch`)
2. Execute `g++ -o kspRfTool kspRfOutlet.cpp -I/usr/local/include -lwiringPi -I/home/pi/RaspberryNewRemoteSwitch` (replace the last one with your path)
3. After this, install paho-mqtt for python (`python3 -m pip install paho-mqtt`)
4. Just run `python3 script.py` to let it run.

## Notes
1. Pin for the RF transmiter is in the `kspRfOutlet.cpp`


