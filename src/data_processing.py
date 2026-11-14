
"""
Data processing module
5G Printed Antenna Optimization
"""

import pandas as pd


def load_dataset(file_path):
    """Load antenna simulation data from a CSV file."""
    data = pd.read_csv(file_path)
    return data


def inspect_dataset(data):
    """Display basic information about the dataset."""
    print(data.head())
    print(data.info())
    print(data.isnull().sum())


if __name__ == "__main__":
    print("Data processing module initialized.")
