from analysis.publisher_analysis import PublisherAnalysis


def test_publisher_analysis_result(sample_clean_data):
    analysis = PublisherAnalysis()
    result = analysis.get_result(sample_clean_data)

    publisher_counts = dict(zip(result["Publisher"], result["Number of Books"]))

    assert list(result.columns) == ["Publisher", "Number of Books"]
    assert publisher_counts["Publisher A"] == 3
    assert publisher_counts["Publisher B"] == 2
    assert publisher_counts["Publisher C"] == 1
    assert publisher_counts["Unknown Publisher"] == 1


def test_publisher_analysis_uses_top_limit(sample_clean_data):
    analysis = PublisherAnalysis(top_limit=2)
    result = analysis.get_result(sample_clean_data)

    assert len(result) == 2
    assert list(result["Publisher"]) == ["Publisher A", "Publisher B"]
