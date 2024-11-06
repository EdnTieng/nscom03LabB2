import matplotlib.pyplot as plt
# TDMA Simulation Parameters
num_stations = 4
total_time = 10  # Total time frame duration
slot_duration = total_time / num_stations

# Plot TDMA
fig, ax = plt.subplots(figsize=(8, 4))

for station in range(num_stations):
    # Time range for each station
    start_time = station * slot_duration
    end_time = (station + 1) * slot_duration
    ax.fill_betweenx([0, 1], start_time, end_time, label=f'Station {station + 1}', alpha=0.7)

# Customize plot
ax.set_title('TDMA (Time Division Multiple Access)')
ax.set_xlabel('Time')
ax.set_ylabel('Frequency')
ax.set_yticks([])
ax.legend()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
