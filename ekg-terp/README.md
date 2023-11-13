# ekg-terp

AI EKG Interpretation

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

# EKG Interpretation Project

## Overview

This project aims to develop an automated tool for interpreting electrocardiogram (EKG) data using machine learning techniques. It involves preprocessing the MIT-BIH Arrhythmia Database, exploratory data analysis, feature extraction, model training, and evaluation.

## Data Preprocessing

The EKG signal data from `.dat` files are preprocessed to remove noise and normalize the signals. Each heartbeat is segmented for further analysis.

### Scripts

- `load_data.py`: Loads EKG data segments from `.npy` files.
- `visualize_data.py`: Generates plots of EKG segments for visual inspection.
- `statistical_analysis.py`: Calculates and outputs basic statistics of the segments.
- `main_analysis.py`: Main script that orchestrates the loading, visualization, and statistical analysis of EKG data.

## Data Exploration and Analysis

Data exploration includes visual inspection and statistical analysis of the preprocessed EKG segments. This phase ensures the data quality and informs further modeling steps.

### Findings

- The mean of the segments is close to zero, indicating successful normalization.
- The standard deviation of the segments suggests a normal level of variability within EKG data.

### Visualizations

- Plots are generated to visually inspect the individual EKG segments.
- Currently, plots are not saved to files as they are used for inline inspection.

## Next Steps

- Feature extraction and selection based on the analysis findings.
- Model training and validation to develop an EKG interpretation model.
- Model evaluation using appropriate medical diagnostic performance metrics.

## Running the Scripts

To run the analysis pipeline, ensure you are in the project's root directory and activate your virtual environment. Then execute the following command:

````bash
python src/main_analysis.py```

````

This will load the data, perform analysis, and output basic statistics to the console.
