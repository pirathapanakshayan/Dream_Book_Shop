from analysis.top_authors_analysis import TopAuthorsAnalysis


def test_top_authors_result(sample_clean_data):
    analysis = TopAuthorsAnalysis()
    result = analysis.get_result(sample_clean_data)

    author_counts = dict(zip(result["Author"], result["Number of Books"]))

    assert list(result.columns) == ["Author", "Number of Books"]
    assert result.iloc[0]["Author"] == "Alice Writer"
    assert result.iloc[0]["Number of Books"] == 3
    assert author_counts["Bob Writer"] == 2
    assert author_counts["Cara Writer"] == 1
    assert author_counts["Unknown Author"] == 1
