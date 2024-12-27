import numpy as np
import matplotlib.pyplot as plt
import time

# Constants
c = 3e8  # Speed of light (m/s)
frequency = 1e6  # Radar frequency (1 MHz)
sampling_rate = 1e7  # Sampling rate (10 MHz)
signal_duration = 1e-3  # Signal duration (1 ms)

# Time array
t = np.linspace(0, signal_duration, int(sampling_rate * signal_duration))

# Generate radar signal
signal = np.sin(2 * np.pi * frequency * t)

# Real-time simulation
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
line, = ax.plot(t, signal, label="Radar Signal")
ax.set_ylim(-1.5, 1.5)
ax.set_title("Real-Time Radar Signal Simulation")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")
ax.legend()

for _ in range(100):  # Simulate 100 iterations
    noise = np.random.normal(0, 0.5, len(t))
    noisy_signal = signal + noise
    line.set_ydata(noisy_signal)
    plt.pause(0.1)  # Update every 0.1 seconds

plt.ioff()
plt.show()
