import numpy as np
import matplotlib.pyplot as plt

# Parameters for simulation
num_nodes = 10                # Number of nodes in the network
num_slots = 50                # Number of time slots for simulation
transmission_probability = 0.3 # Probability a node will attempt to transmit in a given slot

# Initialize arrays
backoff_times = np.zeros(num_nodes, dtype=int)  # Array for node backoff times
successful_transmissions = 0
collisions = 0

# Array to record outcomes for each time slot: 1 for success, -1 for collision, 0 for idle
slot_results = np.zeros(num_slots)

for slot in range(num_slots):
    # Determine which nodes are ready to transmit (backoff time of 0)
    ready_nodes = np.where(backoff_times == 0)[0]
    
    # Nodes transmit based on probability and backoff condition
    transmissions = ready_nodes[np.random.rand(len(ready_nodes)) < transmission_probability]

    # Check transmission outcomes
    if len(transmissions) == 1:
        # Successful transmission
        successful_transmissions += 1
        slot_results[slot] = 1  # Mark successful transmission for this slot
    elif len(transmissions) > 1:
        # Collision
        collisions += 1
        slot_results[slot] = -1  # Mark collision for this slot
        # Set random backoff times for nodes involved in the collision
        backoff_times[transmissions] = np.random.randint(1, 10, size=len(transmissions))
    
    # Decrement backoff times for all nodes with pending backoff
    backoff_times = np.maximum(backoff_times - 1, 0)

# Plotting results
plt.figure(figsize=(15, 6))

# Color-coded bar plot for each slot
colors = ['green' if result == 1 else 'red' if result == -1 else 'gray' for result in slot_results]
plt.bar(range(num_slots), [1] * num_slots, color=colors, edgecolor='black', alpha=0.7)

# Labels and Title
plt.xlabel("Time Slots")
plt.ylabel("Transmission Outcome")
plt.title("CSMA/CD Transmission Outcomes by Time Slot")
plt.yticks([])
plt.xticks(range(0, num_slots, 5))
plt.legend(handles=[
    plt.Line2D([0], [0], color="green", lw=4, label="Successful Transmission"),
    plt.Line2D([0], [0], color="red", lw=4, label="Collision"),
    plt.Line2D([0], [0], color="gray", lw=4, label="Idle Slot")
])

plt.show()
