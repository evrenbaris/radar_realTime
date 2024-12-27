# Mark detected targets in the graph
for _ in range(100):
    noise = np.random.normal(0, 0.5, len(t))
    noisy_signal = signal + noise
    
    target_indices = np.where(noisy_signal > threshold)[0]
    if len(target_indices) > 0:
        target_times = t[target_indices]
        ax.scatter(target_times, noisy_signal[target_indices], color='red', label='Detected Targets')
    
    line.set_ydata(noisy_signal)
    plt.pause(0.1)

plt.ioff()
plt.show()
