import matplotlib.pyplot as plt

def plot_segments(segments, num_to_plot=5):
    plt.figure(figsize=(12, 6))
    for i in range(num_to_plot):
        plt.subplot(num_to_plot, 1, i + 1)
        plt.plot(segments[i])
        plt.title(f"Segment {i+1}")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()
