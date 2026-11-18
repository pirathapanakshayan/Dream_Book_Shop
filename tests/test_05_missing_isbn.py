import pytest

from analysis.missing_isbn_analysis import MissingIsbnAnalysis


def test_missing_isbn_result(sample_clean_data):
    analysis = MissingIsbnAnalysis()
    result = analysis.get_result(sample_clean_data)

    status_table = result.set_index("ISBN Status")

    assert list(result.columns) == ["ISBN Status", "Count", "Percentage"]
    assert status_table.loc["With ISBN", "Count"] == 4
    assert status_table.loc["Without ISBN", "Count"] == 3
    assert status_table.loc["Total Books", "Count"] == 7
    assert status_table.loc["With ISBN", "Percentage"] == pytest.approx(57.14)
    assert status_table.loc["Without ISBN", "Percentage"] == pytest.approx(42.86)
    assert status_table.loc["Total Books", "Percentage"] == pytest.approx(100.0)
