import numpy as np
import matplotlib.pyplot as plt

# Generate Walsh codes for channelization
def walsh_matrix(n):
    """Generate Walsh matrix of size 2^n x 2^n."""
    if n == 0:
        return np.array([[1]])
    else:
        smaller_matrix = walsh_matrix(n - 1)
        top = np.hstack((smaller_matrix, smaller_matrix))
        bottom = np.hstack((smaller_matrix, -smaller_matrix))
        return np.vstack((top, bottom))

# Parameters
num_users = 4  # Number of users (must be a power of 2 for Walsh matrix)
message_length = 8  # Number of bits per user

# Generate Walsh matrix for user codes
n = int(np.log2(num_users))
walsh_codes = walsh_matrix(n)

# Repeat Walsh codes to match the message length
walsh_codes = np.repeat(walsh_codes, message_length // num_users, axis=1)

# Simulate random binary messages for each user
user_signals = 2 * np.random.randint(0, 2, (num_users, message_length)) - 1  # Convert {0,1} to {-1,1}

# Spread each user's signal using their unique Walsh code
spread_signals = np.array([user_signals[i] * walsh_codes[i] for i in range(num_users)])

# Aggregate the spread signals to form the combined CDMA signal
cdma_signal = np.sum(spread_signals, axis=0)

# Plotting
fig, axs = plt.subplots(num_users + 1, 1, figsize=(10, 2 * (num_users + 1)))

# Plot each user's original and spread signal
for i in range(num_users):
    axs[i].stem(user_signals[i], linefmt=f"C{i}-", markerfmt=f"C{i}o", basefmt="k")
    axs[i].set_title(f"User {i + 1} Signal (Original)")
    axs[i].set_ylim([-2, 2])

# Plot the combined CDMA signal
axs[-1].stem(cdma_signal, linefmt="C0-", markerfmt="C0o", basefmt="k")
axs[-1].set_title("Combined CDMA Signal (Sum of Spread Signals)")
axs[-1].set_ylim([-num_users, num_users])

plt.tight_layout()
plt.show()
