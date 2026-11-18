import re
from datetime import date, datetime

import pandas as pd


# Caption: OOP is used here because DataCleaner is a class with cleaning methods.
# SOLID - SRP: This class only cleans data. It does not load, validate, or analyse data.
class DataCleaner:
    """OOP class for preparing the book dataset before analysis."""

    def clean_data(self, data):
        """Step by step: fill missing text, create publication_year, and remove bad years."""
        # Step 1: Copy the data so the original DataFrame is not changed.
        cleaned_data = data.copy()

        # Step 2: Fill missing text values needed for analysis.
        self._fill_missing_text(cleaned_data, "author", "Unknown Author")
        self._fill_missing_text(cleaned_data, "language", "Unknown Language")
        self._fill_missing_text(cleaned_data, "book publisher", "Unknown Publisher")

        # Step 3: Create a new column called publication_year.
        cleaned_data["publication_year"] = cleaned_data["publication date"].apply(
            self._extract_year
        )

        # Step 4: Remove rows where a publication year cannot be found.
        cleaned_data = cleaned_data.dropna(subset=["publication_year"]).copy()

        # Step 5: Convert the year into an integer value.
        cleaned_data["publication_year"] = cleaned_data["publication_year"].astype(int)

        return cleaned_data

    def _fill_missing_text(self, data, column_name, replacement_text):
        """Step by step: replace empty text in one column with a default value."""
        # Step 1: Replace missing values such as NaN.
        data[column_name] = data[column_name].fillna(replacement_text)

        # Step 2: Convert values to text and remove extra spaces.
        data[column_name] = data[column_name].astype(str).str.strip()

        # Step 3: Replace blank text values.
        data.loc[data[column_name] == "", column_name] = replacement_text

    def _extract_year(self, value):
        """Step by step: extract a four-digit year from a date value."""
        # Step 1: If the value is missing, return None.
        if pd.isna(value):
            return None

        # Step 2: If pandas or Python already understands the date, return its year.
        if isinstance(value, (datetime, date, pd.Timestamp)):
            return value.year

        # Step 3: Convert the value to text and search for a four-digit year.
        text_value = str(value).strip()
        year_match = re.search(r"\b(\d{4})\b", text_value)

        # Step 4: If a year is found, return it as an integer.
        if year_match:
            return int(year_match.group(1))

        # Step 5: If no year is found, return None.
        return None
