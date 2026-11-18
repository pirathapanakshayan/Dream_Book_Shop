import matplotlib.pyplot as plt

from analysis.base_analysis import BaseAnalysis


# Caption: Strategy Pattern - this is one concrete analysis strategy.
# OOP - Inheritance: This class inherits from BaseAnalysis.
# SOLID - SRP: This class only handles language distribution analysis.
class LanguageDistributionAnalysis(BaseAnalysis):
    """Analysis class for counting books by language."""

    def get_result(self, data):
        """Step by step: count how many books are in each language."""
        # Step 1: Group the DataFrame by language and count rows.
        language_counts = data.groupby("language").size().sort_values(ascending=False)

        # Step 2: Convert the pandas Series into a DataFrame.
        result = language_counts.reset_index(name="Number of Books")

        # Step 3: Rename the column for a clear table heading.
        result = result.rename(columns={"language": "Language"})

        return result

    def show_table(self, result):
        """Step by step: show language distribution as a terminal table."""
        # Step 1: Use the common print_table helper from BaseAnalysis.
        self.print_table("Language Distribution of Books", result)

    def show_graph(self, result):
        """Step by step: show language distribution as a bar chart."""
        # Step 1: Create the graph area.
        plt.figure(figsize=(10, 6))

        # Step 2: Draw a bar chart with languages on the x-axis.
        plt.bar(result["Language"], result["Number of Books"], label="Books")

        # Step 3: Add title, axis labels, rotated x labels, and legend.
        plt.title("Language Distribution of Books")
        plt.xlabel("Language")
        plt.ylabel("Number of Books")
        plt.xticks(rotation=45, ha="right")
        plt.legend()

        # Step 4: Adjust spacing and show the graph.
        plt.tight_layout()
        plt.show()
