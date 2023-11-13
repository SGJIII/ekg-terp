import numpy as np
from utils.load_data import load_all_segments
from visualization.visualize_data import plot_segments
from analysis.statistical_analysis import analyze_segments

directory_path = 'data/processed/ekg_segments'  # Input directory
output_dir = 'output/analysis_outputs'  # Output directory for segments

# Load all segments
all_segments = load_all_segments(directory_path)

# Visualize a few segments
plot_segments(all_segments)

# Perform statistical analysis
means, std_devs = analyze_segments(all_segments)

# Print or save the analysis results
print("Mean of segments:", np.mean(means))
print("Standard deviation of segments:", np.mean(std_devs))
# Further analysis and documentation
