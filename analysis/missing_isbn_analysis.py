import matplotlib.pyplot as plt
import pandas as pd

from analysis.base_analysis import BaseAnalysis


# Caption: Strategy Pattern - this is one concrete analysis strategy.
# OOP - Inheritance: This class inherits from BaseAnalysis.
# SOLID - SRP: This class only handles missing ISBN analysis.
class MissingIsbnAnalysis(BaseAnalysis):
    """Analysis class for checking books with and without ISBN values."""

    def get_result(self, data):
        """Step by step: count books with ISBN and without ISBN."""
        # Step 1: Keep ISBN missing values useful by checking them here.
        isbn_values = data["ISBN"].fillna("").astype(str).str.strip()

        # Step 2: Create a pandas Series with True for rows that have ISBN values.
        has_isbn = isbn_values != ""

        # Step 3: Count total books, books with ISBN, and books without ISBN.
        total_books = len(data)
        with_isbn_count = int(has_isbn.sum())
        without_isbn_count = total_books - with_isbn_count

        # Step 4: Create the result DataFrame with counts and percentages.
        result = pd.DataFrame(
            {
                "ISBN Status": ["With ISBN", "Without ISBN", "Total Books"],
                "Count": [with_isbn_count, without_isbn_count, total_books],
                "Percentage": [
                    self._calculate_percentage(with_isbn_count, total_books),
                    self._calculate_percentage(without_isbn_count, total_books),
                    100.0 if total_books > 0 else 0.0,
                ],
            }
        )

        return result

    def show_table(self, result):
        """Step by step: show missing ISBN analysis as a terminal table."""
        # Step 1: Use the common print_table helper from BaseAnalysis.
        self.print_table("Missing ISBN Analysis", result)

    def show_graph(self, result):
        """Step by step: show ISBN status as a pie chart."""
        # Step 1: Remove the Total Books row because pie chart needs only the two parts.
        pie_data = result[result["ISBN Status"] != "Total Books"]

        # Step 2: Create the graph area.
        plt.figure(figsize=(8, 8))

        # Step 3: Draw a pie chart with percentages.
        plt.pie(
            pie_data["Count"],
            labels=pie_data["ISBN Status"],
            autopct="%1.1f%%",
            startangle=90,
        )

        # Step 4: Add title and show the graph.
        plt.title("Missing ISBN Analysis")
        plt.tight_layout()
        plt.show()

    def _calculate_percentage(self, count, total):
        """Step by step: calculate percentage safely."""
        # Step 1: Avoid division by zero when there are no books.
        if total == 0:
            return 0.0

        # Step 2: Calculate and round the percentage.
        return round((count / total) * 100, 2)
