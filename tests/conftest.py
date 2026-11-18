import sys
from pathlib import Path

import matplotlib
import pandas as pd
import pytest

matplotlib.use("Agg")

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from data_cleaner import DataCleaner


@pytest.fixture
def sample_raw_data():
    return pd.DataFrame(
        {
            "book": [
                "Book A",
                "Book B",
                "Book C",
                "Book D",
                "Book E",
                "Book F",
                "Book G",
                "Book H",
            ],
            "author": [
                "Alice Writer",
                "Bob Writer",
                "Alice Writer",
                "Cara Writer",
                "Alice Writer",
                "Bob Writer",
                None,
                "",
            ],
            "publication date": [
                "2020-05-10",
                "2020",
                "2021-03-01",
                "2021",
                "2022",
                "2022-07-01",
                "2022",
                "not a date",
            ],
            "language": [
                "English",
                "English",
                "Sinhala",
                "Tamil",
                "English",
                "Sinhala",
                "",
                None,
            ],
            "book publisher": [
                "Publisher A",
                "Publisher B",
                "Publisher A",
                "Publisher C",
                "Publisher A",
                "Publisher B",
                None,
                "Publisher D",
            ],
            "ISBN": ["111", "", None, "444", "555", " ", "777", "888"],
            "BNB id": [
                "BNB1",
                "BNB2",
                "BNB3",
                "BNB4",
                "BNB5",
                "BNB6",
                "BNB7",
                "BNB8",
            ],
        }
    )


@pytest.fixture
def sample_clean_data(sample_raw_data):
    cleaner = DataCleaner()
    return cleaner.clean_data(sample_raw_data)
