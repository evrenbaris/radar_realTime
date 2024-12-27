# Dynamic target detection (example with thresholding)
threshold = 0.8

for _ in range(100):  # Simulate 100 iterations
    noise = np.random.normal(0, 0.5, len(t))
    noisy_signal = signal + noise
    
    # Detect targets exceeding threshold
    target_indices = np.where(noisy_signal > threshold)[0]
    if len(target_indices) > 0:
        target_times = t[target_indices]
        print(f"Targets detected at times: {target_times}")

    line.set_ydata(noisy_signal)
    plt.pause(0.1)

plt.ioff()
plt.show()
