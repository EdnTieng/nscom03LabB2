import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_nodes = 5                 # Number of nodes
num_slots = 30                # Number of time slots to simulate
transmission_probability = 0.3 # Probability a node will start RTS

# Arrays to keep track of states and results
backoff_times = np.zeros(num_nodes, dtype=int)  # Backoff times for each node
slot_results = np.zeros(num_slots)              # Slot results (0 for idle, 1 for success, -1 for collision)

# Counters
successful_exchanges = 0
collisions = 0

for slot in range(num_slots):
    ready_nodes = np.where(backoff_times == 0)[0]  # Nodes with zero backoff

    # Nodes initiate RTS based on probability
    rts_nodes = ready_nodes[np.random.rand(len(ready_nodes)) < transmission_probability]

    # Collision if multiple nodes send RTS at the same time
    if len(rts_nodes) == 1:
        # Successful RTS; initiate CTS, Data, ACK
        node_id = rts_nodes[0]
        slot_results[slot] = 1  # Mark slot as success
        successful_exchanges += 1

        # Reset backoff for the node
        backoff_times[node_id] = np.random.randint(1, 10)

        # Simulate CTS, Data, ACK within the same slot for simplicity
        # In real scenarios, these would each take time slots
        
    elif len(rts_nodes) > 1:
        # Collision due to multiple RTS
        collisions += 1
        slot_results[slot] = -1  # Mark slot as collision

        # Assign random backoff times to nodes involved in the collision
        backoff_times[rts_nodes] = np.random.randint(1, 10, size=len(rts_nodes))

    # Decrement backoff for all other nodes
    backoff_times = np.maximum(backoff_times - 1, 0)

# Plotting the results
plt.figure(figsize=(12, 6))

# Color-coded slots
colors = ['green' if result == 1 else 'red' if result == -1 else 'gray' for result in slot_results]
plt.bar(range(num_slots), [1] * num_slots, color=colors, edgecolor='black', alpha=0.7)

# Labels and Title
plt.xlabel("Time Slots")
plt.ylabel("Frame Exchange Outcome")
plt.title("CSMA/CA Frame Exchange Simulation (RTS/CTS/Data/ACK)")
plt.yticks([])
plt.xticks(range(0, num_slots, 5))
plt.legend(handles=[
    plt.Line2D([0], [0], color="green", lw=4, label="Successful Exchange"),
    plt.Line2D([0], [0], color="red", lw=4, label="Collision"),
    plt.Line2D([0], [0], color="gray", lw=4, label="Idle Slot")
])

plt.show()
