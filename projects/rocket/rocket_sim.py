import numpy as np
import pandas as pd

dt = 0.1
time = np.arange(0,30,dt)

altitude = []
velocity = []
acceleration = []

v = 0
h = 0

for t in time:
    if t < 3:
        a = 35 # boost
    elif t < 12:
        a = -9.81 # coast (g)
    elif t < 15:
        a = -3 # parachute
    else:
        a = -1 # descent
        
    v = v + a * dt
    h = max(0, h + v * dt)
    
    acceleration.append(a)
    velocity.append(v)
    altitude.append(h)
    
df = pd.DataFrame({
    "time_s": time,
    "altitude_m": altitude,
    "velocity_m_s": velocity,
    "acceleration_m_s2": acceleration
                      })
df.to_csv("rocket_flight.csv", index=False)

print(df.head())
print("Flight Saved.")

