import pytest

from column_validator import REQUIRED_COLUMNS, ColumnValidator


def test_required_columns_pass_validation(sample_raw_data):
    validator = ColumnValidator()

    assert validator.validate(sample_raw_data) is True


def test_missing_required_column_raises_error(sample_raw_data):
    validator = ColumnValidator()
    data_without_author = sample_raw_data.drop(columns=["author"])

    with pytest.raises(ValueError, match="Missing required column"):
        validator.validate(data_without_author)


def test_required_columns_are_stored_in_a_list():
    assert isinstance(REQUIRED_COLUMNS, list)
    assert "book" in REQUIRED_COLUMNS
    assert "publication date" in REQUIRED_COLUMNS
    assert "ISBN" in REQUIRED_COLUMNS
