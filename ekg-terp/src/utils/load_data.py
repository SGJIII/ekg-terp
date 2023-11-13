import numpy as np
import os

def load_all_segments(directory_path):
    all_segments = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.npy'):
            file_path = os.path.join(directory_path, filename)
            segments = np.load(file_path)
            all_segments.append(segments)
    return np.concatenate(all_segments)
