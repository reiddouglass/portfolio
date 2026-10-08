import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("flight.csv")

plt.plot(
    data["time"],
    data["altitude"]
         )
plt.xlabel("Time")
plt.ylabel("Altitude")
plt.title("Simulated Flight")

plt.show()
