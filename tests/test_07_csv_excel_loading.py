import pandas as pd
import pytest

from data_loader import DataLoader


def test_csv_and_excel_loading(tmp_path):
    data = pd.DataFrame(
        {
            "book": ["Book A"],
            "author": ["Alice Writer"],
            "publication date": ["2020"],
            "language": ["English"],
            "book publisher": ["Publisher A"],
            "ISBN": ["111"],
            "BNB id": ["BNB1"],
        }
    )

    csv_file = tmp_path / "books.csv"
    excel_file = tmp_path / "books.xlsx"

    data.to_csv(csv_file, index=False)
    data.to_excel(excel_file, index=False)

    loader = DataLoader()
    csv_data = loader.load_data(csv_file)
    excel_data = loader.load_data(excel_file)

    assert csv_data.shape == (1, 7)
    assert excel_data.shape == (1, 7)
    assert list(csv_data.columns) == list(data.columns)
    assert list(excel_data.columns) == list(data.columns)


def test_unsupported_file_type_raises_error(tmp_path):
    text_file = tmp_path / "books.txt"
    text_file.write_text("not a dataset")

    loader = DataLoader()

    with pytest.raises(ValueError, match="Unsupported file type"):
        loader.load_data(text_file)
