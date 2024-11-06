import random
import matplotlib.pyplot as plt

# Simulation parameters
num_stations = 4  # Number of stations
num_frames = 6  # Number of frames each station sends
frame_duration = 1  # Duration of each frame in seconds
total_time = 10  # Total simulation time in seconds
slot_duration = frame_duration  # Slot duration for slotted ALOHA
collision_color = 'gray'  # Color to indicate collisions

# Generate start times aligned with time slots for each station's frames in Slotted ALOHA
slotted_transmissions = {station: [] for station in range(1, num_stations + 1)}
for station in slotted_transmissions:
    for _ in range(num_frames):
        slot_number = random.randint(0, int(total_time // slot_duration) - 1)
        start_time = slot_number * slot_duration
        slotted_transmissions[station].append((start_time, start_time + frame_duration))

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

# Plotting Slotted ALOHA
fig, ax = plt.subplots(figsize=(12, 6))
colors = ['yellow', 'lightblue', 'lightgreen', 'lightpink']
for station, frames in slotted_transmissions.items():
    for i, (start, end) in enumerate(frames):
        ax.plot([start, end], [station, station], color=colors[station - 1], lw=5)
        if i % 2 == 0:
            ax.text((start + end) / 2, station + 0.2, f"Frame{i + 1}.{station}", ha='center', va='bottom')
        else:
            ax.text((start + end) / 2, station - 0.2, f"Frame {i + 1}.{station}", ha='center', va='top')

# Add time slots for visual reference
for slot in range(int(total_time // slot_duration) + 1):
    ax.axvline(slot * slot_duration, color='black', linestyle='--', linewidth=0.8)

# Detect and plot collisions for Slotted ALOHA
slotted_collisions = detect_collisions(slotted_transmissions)
for frame1, frame2 in slotted_collisions:
    ax.axvspan(max(frame1[0], frame2[0]), min(frame1[1], frame2[1]), color=collision_color, alpha=0.5)

# Customize Slotted ALOHA plot
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Station')
ax.set_title('Frames in Slotted ALOHA Network with Time Slots')
ax.set_yticks(range(1, num_stations + 1))
ax.set_ylim(0.5, num_stations + 0.5)
ax.grid(True)
plt.show()
