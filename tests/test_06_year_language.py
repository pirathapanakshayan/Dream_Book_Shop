import pandas as pd

from analysis.year_language_analysis import YearLanguageAnalysis


def test_year_language_result(sample_clean_data):
    analysis = YearLanguageAnalysis()
    result = analysis.get_result(sample_clean_data)

    expected_rows = {
        (2020, "English", 2),
        (2021, "Sinhala", 1),
        (2021, "Tamil", 1),
        (2022, "English", 1),
        (2022, "Sinhala", 1),
        (2022, "Unknown Language", 1),
    }

    actual_rows = set(
        tuple(row)
        for row in result[["Year", "Language", "Number of Books"]].to_numpy()
    )

    assert list(result.columns) == ["Year", "Language", "Number of Books"]
    assert actual_rows == expected_rows


def test_year_language_result_uses_top_10_languages():
    rows = []
    for index in range(12):
        language = f"Language {index + 1}"
        rows.extend(
            {"publication_year": 2024, "language": language}
            for _ in range(12 - index)
        )

    analysis = YearLanguageAnalysis()
    result = analysis.get_result(pd.DataFrame(rows))
    languages = set(result["Language"])

    assert len(languages) == 10
    assert "Language 10" in languages
    assert "Language 11" not in languages
    assert "Language 12" not in languages
