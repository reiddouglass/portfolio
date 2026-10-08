import json
import paho.mqtt.client as mqtt
import pandas as pd
import matplotlib.pyplot as plt


def on_message(client, userdata, msg)
    data = json.loads(msg.payload)
    
    altitude = data["altitude"]
    velocity = data["velocity"]
    
    print(altitude, velocity)

client = mqtt.Client()

client.connect("ip", 1883)

client.subscribe("rocket/telemetry")
client.on_message = on_message
client.loop(60)

fig, axs = plt.subplots(2, 2, figsize=(12, 6))

axs[0,0].plot(df["time_s"], df["altitude_m"])
axs[0,0].set_xlabel("Time (s)")
axs[0,0].set_ylabel("Altitude (m)")
axs[0,0].set_title("Rocket Altitude vs Time")
axs[0,0].grid(True)

axs[0,1].plot(df["time_s"], df["velocity_m_s"])
axs[0,1].set_xlabel("Time (s)")
axs[0,1].set_ylabel("Velocity (m/s)")
axs[0,1].set_title("Rocket Velocity vs Time")
plt.grid(True)

axs[1,0].plot(df["time_s"], df["acceleration_m_s2"])
axs[1,0].set_xlabel("Time (s)")
axs[1,0].set_ylabel("Acceleration (m/s²)")
axs[1,0].set_title("Rocket Acceleration vs Time")
plt.grid(True)

plt.tight_layout()
plt.savefig("Telemetry.png")

plt.show()

max_altitude = df["altitude_m"].max()
time_apogee = df.loc[df["altitude_m"].idxmax(), "time_s"]
max_velocity = df["velocity_m_s"].max()
max_acceleration = df["acceleration_m_s2"].max()

print(f"Max altitude: {max_altitude:.2f} m")
print(f"Time to apogee: {time_apogee:.2f} s")
print(f"Max velocity: {max_velocity:.2f} m/s")
print(f"Max acceleration: {max_acceleration:.2f} m/s²")
