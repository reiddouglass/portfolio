6/3
Still out of town
During airport layover, started on backend with stand-in flight simulator
Simulator prints to CSV file. Analyze_flight.py pulls data from CSV table and outputs 3 graphs in 2x2 grid : Altitude vs Time, Velocity vs Time, Acceleration vs Time. These are printed onto one Telemetry.png file.
Some Flight details are printed:
Max altitude, time to apogee, max velo & accel
Future replacements: Basically complete overhaul
After homelab is set up: 
- Create MSQTT Broker on Home Assistant
- Send Publish flight simulation data to broker : replaces CSV file
- Python graphs: Flight analyzer subscribes to MSQTT data to display graphs
- Homelab graphs: Grafana reads data from MSQTT Broker
- Replace Flight simulator with ESP32 Simulator 
- Take ESP32 hiking or simulate a flight some other way
- Alert system: High temp, High pressure, lost signal, sensor failure
- Event Detection: Launch, Apogee, Parachute Deploy, Landing
MQTT Publishes: Altitude, Velocity, Accel,  Alerts, Events? (can be calculated)

End goal stack:
Simulator/ESP32
 ↓
MQTT
 ↓
InfluxDB
 ↓
Grafana
- Side project from ESP32 : Portable Hike/Run/walk logger
    -Total Distance (x distance, y altitude change)
    -Location/GPS?? on it maybe
    -Doubles as hike logger, data can be amplified for Flight simulation
