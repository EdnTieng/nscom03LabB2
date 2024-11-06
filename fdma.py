import matplotlib.pyplot as plt

# FDMA Simulation Parameters
num_stations = 4
total_bandwidth = 10  # Total frequency range
bandwidth_per_station = total_bandwidth / num_stations

# Plot FDMA
fig, ax = plt.subplots(figsize=(8, 4))

for station in range(num_stations):
    # Frequency range for each station
    start_freq = station * bandwidth_per_station
    end_freq = (station + 1) * bandwidth_per_station
    ax.fill_between([0, 10], start_freq, end_freq, label=f'Station {station + 1}', alpha=0.7)

# Customize plot
ax.set_title('FDMA (Frequency Division Multiple Access)')
ax.set_xlabel('Time')
ax.set_ylabel('Frequency')
ax.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
