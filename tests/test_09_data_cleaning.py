import pandas as pd

from data_cleaner import DataCleaner


def test_data_cleaning_creates_publication_year(sample_raw_data):
    cleaner = DataCleaner()
    result = cleaner.clean_data(sample_raw_data)

    assert "publication_year" in result.columns
    assert list(result["publication_year"]) == [2020, 2020, 2021, 2021, 2022, 2022, 2022]


def test_data_cleaning_removes_rows_without_valid_year(sample_raw_data):
    cleaner = DataCleaner()
    result = cleaner.clean_data(sample_raw_data)

    assert len(result) == 7
    assert "Book H" not in list(result["book"])


def test_data_cleaning_fills_required_missing_text(sample_raw_data):
    cleaner = DataCleaner()
    result = cleaner.clean_data(sample_raw_data)

    book_g = result[result["book"] == "Book G"].iloc[0]

    assert book_g["author"] == "Unknown Author"
    assert book_g["language"] == "Unknown Language"
    assert book_g["book publisher"] == "Unknown Publisher"


def test_data_cleaning_keeps_missing_isbn_values(sample_raw_data):
    cleaner = DataCleaner()
    result = cleaner.clean_data(sample_raw_data)

    book_b_isbn = result.loc[result["book"] == "Book B", "ISBN"].iloc[0]
    book_c_isbn = result.loc[result["book"] == "Book C", "ISBN"].iloc[0]

    assert book_b_isbn == ""
    assert pd.isna(book_c_isbn)
