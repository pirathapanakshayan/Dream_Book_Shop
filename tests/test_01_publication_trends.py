import pandas as pd

from analysis.publication_trends_analysis import PublicationTrendsAnalysis


def test_publication_trends_result(sample_clean_data):
    analysis = PublicationTrendsAnalysis()
    result = analysis.get_result(sample_clean_data)

    expected_result = pd.DataFrame(
        {"Year": [2020, 2021, 2022], "Number of Books": [2, 2, 3]}
    )

    pd.testing.assert_frame_equal(result, expected_result)
