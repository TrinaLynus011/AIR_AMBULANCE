import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("altitude_log.csv")
plt.plot(df.step, df.altitude_ft, label="Altitude")
plt.xlabel("Time step")
plt.ylabel("Altitude (ft)")
plt.title("Air Ambulance Altitude over Simulation")
plt.grid(True)
plt.legend()
plt.show()
