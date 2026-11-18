from analysis.language_distribution_analysis import LanguageDistributionAnalysis


def test_language_distribution_result(sample_clean_data):
    analysis = LanguageDistributionAnalysis()
    result = analysis.get_result(sample_clean_data)

    language_counts = dict(zip(result["Language"], result["Number of Books"]))

    assert list(result.columns) == ["Language", "Number of Books"]
    assert language_counts["English"] == 3
    assert language_counts["Sinhala"] == 2
    assert language_counts["Tamil"] == 1
    assert language_counts["Unknown Language"] == 1
