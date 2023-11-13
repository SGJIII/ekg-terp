import os
import wfdb
import numpy as np
from scipy.signal import butter, filtfilt

def load_ekg_data(record_path):
    record = wfdb.rdrecord(record_path)
    signal = record.p_signal[:,0]  # Assuming single-lead EKG
    fs = record.fs  # Sampling frequency
    return signal, fs

def bandpass_filter(signal, lowcut, highcut, fs, order=2):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal

def normalize_signal(signal):
    norm_signal = (signal - np.mean(signal)) / np.std(signal)
    return norm_signal

def segment_signal(signal, annotations, fs, window_size=1.0):
    segments = []
    for ann_index in annotations.sample:  # Iterate over annotation indices
        start = int(max(ann_index - window_size * fs / 2, 0))
        end = int(min(start + window_size * fs, len(signal)))
        segment = signal[start:end]
        if len(segment) == window_size * fs:
            segments.append(segment)
    return np.array(segments)

def preprocess_ekg(record_path):
    signal, fs = load_ekg_data(record_path)
    filtered_signal = bandpass_filter(signal, lowcut=0.5, highcut=50, fs=fs)
    normalized_signal = normalize_signal(filtered_signal)

    annotations = wfdb.rdann(record_path, 'atr')
    segments = segment_signal(normalized_signal, annotations, fs, window_size=1.0)

    return segments

def save_segments(segments, output_dir, filename):
    np.save(os.path.join(output_dir, f"{filename}_segments.npy"), segments)

def process_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.dat'):
            record_path = os.path.join(directory_path, filename.split('.')[0])
            try:
                segments = preprocess_ekg(record_path)
                print(f"Processed {len(segments)} segments from {filename}")


                # Save the segments
                save_segments(segments, output_dir, filename.split('.')[0])


            except Exception as e:
                print(f"Error processing file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    directory_path = 'data/raw/mit-bih-arrhythmia-database-1.0.0'  # Replace with the path to your directory
    output_dir = 'data/processed/ekg_segments'  # Output directory for segments
    process_directory(directory_path)
    
