from analysis.language_distribution_analysis import LanguageDistributionAnalysis
from analysis.missing_isbn_analysis import MissingIsbnAnalysis
from analysis.publication_trends_analysis import PublicationTrendsAnalysis
from analysis.publisher_analysis import PublisherAnalysis
from analysis.top_authors_analysis import TopAuthorsAnalysis
from analysis.year_language_analysis import YearLanguageAnalysis


# Caption: Factory Method Pattern is used here.
# The main program asks this factory to create the correct analysis object.
# SOLID - DIP: main.py depends on this factory, not on every analysis class directly.
# SOLID - OCP: To add a new analysis, add a new class and update this mapping.
class AnalysisFactory:
    """Factory class for creating analysis strategy objects."""

    @staticmethod
    def create_analysis(choice):
        """Step by step: receive a menu choice and return the correct analysis object."""
        # Step 1: Dictionary maps menu numbers to analysis classes.
        analysis_map = {
            "1": PublicationTrendsAnalysis,
            "2": TopAuthorsAnalysis,
            "3": LanguageDistributionAnalysis,
            "4": PublisherAnalysis,
            "5": MissingIsbnAnalysis,
            "6": YearLanguageAnalysis,
        }

        # Step 2: Get the class that matches the user's choice.
        analysis_class = analysis_map.get(str(choice))

        # Step 3: Return None when the choice is invalid.
        if analysis_class is None:
            return None

        # Step 4: Create and return the selected analysis object.
        return analysis_class()
