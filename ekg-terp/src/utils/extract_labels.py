import os
import wfdb

def extract_unique_labels(data_directory):
    unique_labels = set()

    for file in os.listdir(data_directory):
        if file.endswith('.atr'):
            record_name = os.path.splitext(file)[0]
            path = os.path.join(data_directory, record_name)
            print(f"Processing file: {path}")  # Debugging print

            try:
                annotation = wfdb.rdann(path, 'atr')
                unique_labels.update(annotation.symbol)
                print(f"Found labels: {annotation.symbol}")  # Debugging print
            except Exception as e:
                print(f"Error processing file {path}: {e}")

    return unique_labels

def write_labels_to_file(labels, output_file):
    with open(output_file, 'w') as file:
        for label in sorted(labels):
            file.write(label + '\n')

# Directory where the MIT-BIH Arrhythmia Database is stored
data_directory = 'data/raw/mit-bih-arrhythmia-database-1.0.0'

# Path for the output file
output_file = 'data/processed/unique_labels.txt'

# Extracting the labels
labels = extract_unique_labels(data_directory)

# Check if labels were extracted
if labels:
    write_labels_to_file(labels, output_file)
    print(f"Unique EKG Labels written to {output_file}")
else:
    print("No labels were extracted. Please check the data directory.")

