import numpy as np

def analyze_segments(segments):
    means = np.mean(segments, axis=1)
    std_devs = np.std(segments, axis=1)
    # Add more statistical analysis as needed
    return means, std_devs
