import random
import csv

time = 0
altitude = 0
velocity = 0

with open("flight.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow([
        "time",
        "altitude",
        "velocity"

                     ])
    writer.writerow([
		time,
		altitude,
		velocity
                ])
    for i in range(3):
        velocity += round(random.uniform(0, 3), 2)
        altitude += velocity
        writer.writerow([
            i+1,
            altitude,
            velocity
                        ])
    for i in range(97):
        velocity += round(random.uniform(-1, 3), 2)
        altitude += velocity
        
        writer.writerow([
            i+3,
            altitude,
            velocity
                         ])
