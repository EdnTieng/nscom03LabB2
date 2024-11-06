import random

import matplotlib.pyplot as plt

# Simulation parameters
num_stations = 4  # Number of stations
num_frames = 6  # Number of frames each station sends
frame_duration = 1  # Duration of each frame in seconds
total_time = 10  # Total simulation time in seconds
collision_color = 'gray'  # Color to indicate collisions

# Generate random start times for each station's frames in Pure ALOHA
pure_transmissions = {station: [] for station in range(1, num_stations + 1)}
for station in pure_transmissions:
    for _ in range(num_frames):
        start_time = random.uniform(0, total_time - frame_duration)
        pure_transmissions[station].append((start_time, start_time + frame_duration))

# Function to detect collisions between frames
def detect_collisions(transmissions):
    collisions = []
    for station1, frames1 in transmissions.items():
        for station2, frames2 in transmissions.items():
            if station1 != station2:
                for frame1 in frames1:
                    for frame2 in frames2:
                        if max(frame1[0], frame2[0]) < min(frame1[1], frame2[1]):
                            # Collision detected
                            collisions.append((frame1, frame2))
    return collisions

# Plotting Pure ALOHA
fig, ax = plt.subplots(figsize=(12, 6))
colors = ['yellow', 'lightblue', 'lightgreen', 'lightpink']
for station, frames in pure_transmissions.items():
    for i, (start, end) in enumerate(frames):
        ax.plot([start, end], [station, station], color=colors[station - 1], lw=5)
        if i % 2 == 0:
            ax.text((start + end) / 2, station + 0.2, f"Frame{i + 1}.{station}", ha='center', va='bottom')
        else:
            ax.text((start + end) / 2, station - 0.2, f"Frame {i + 1}.{station}", ha='center', va='top')

# Detect and plot collisions for Pure ALOHA
pure_collisions = detect_collisions(pure_transmissions)
for frame1, frame2 in pure_collisions:
    ax.axvspan(max(frame1[0], frame2[0]), min(frame1[1], frame2[1]), color=collision_color, alpha=0.5)

# Customize Pure ALOHA plot
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Station')
ax.set_title('Frames in Pure ALOHA Network')
ax.set_yticks(range(1, num_stations + 1))
ax.set_ylim(0.5, num_stations + 0.5)
ax.grid(True)
plt.show()
