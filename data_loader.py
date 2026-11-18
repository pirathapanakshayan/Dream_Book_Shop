from pathlib import Path

import pandas as pd


# Caption: OOP is used here because DataLoader is a class with one clear job.
# SOLID - SRP: This class only loads data. It does not clean or analyse data.
class DataLoader:
    """OOP class for loading CSV and Excel book datasets."""

    def load_data(self, file_path):
        """Step by step: check the file, find its type, and load it with pandas."""
        # Step 1: Convert the file name into a Path object.
        path = Path(file_path)

        # Step 2: Show a clear error if the file does not exist.
        if not path.exists():
            raise FileNotFoundError(f"Dataset file was not found: {file_path}")

        # Step 3: Get the file extension, such as .csv or .xlsx.
        file_extension = path.suffix.lower()

        # Step 4: Load CSV files using pandas read_csv().
        if file_extension == ".csv":
            return pd.read_csv(path)

        # Step 5: Load Excel files using pandas read_excel().
        if file_extension in [".xlsx", ".xls"]:
            return pd.read_excel(path)

        # Step 6: Reject unsupported file types with a friendly error.
        raise ValueError("Unsupported file type. Please use a .csv, .xlsx, or .xls file.")
