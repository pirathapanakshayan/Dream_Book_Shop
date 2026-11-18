import matplotlib.pyplot as plt

from analysis.base_analysis import BaseAnalysis


# Caption: Strategy Pattern - this is one concrete analysis strategy.
# OOP - Inheritance: This class inherits from BaseAnalysis.
# SOLID - SRP: This class only handles top authors analysis.
class TopAuthorsAnalysis(BaseAnalysis):
    """Analysis class for the top 5 most prolific authors."""

    def get_result(self, data):
        """Step by step: count books per author and keep the top 5."""
        # Step 1: Group the DataFrame by author and count rows.
        author_counts = data.groupby("author").size().sort_values(ascending=False)

        # Step 2: Keep only the first 5 authors.
        result = author_counts.head(5).reset_index(name="Number of Books")

        # Step 3: Rename the column for a clear table heading.
        result = result.rename(columns={"author": "Author"})

        return result

    def show_table(self, result):
        """Step by step: show top authors as a terminal table."""
        # Step 1: Use the common print_table helper from BaseAnalysis.
        self.print_table("Top 5 Most Prolific Authors", result)

    def show_graph(self, result):
        """Step by step: show top authors as a bar chart."""
        # Step 1: Create the graph area.
        plt.figure(figsize=(10, 6))

        # Step 2: Draw a bar chart with authors on the x-axis.
        plt.bar(result["Author"], result["Number of Books"], label="Books")

        # Step 3: Add title, axis labels, rotated x labels, and legend.
        plt.title("Top 5 Most Prolific Authors")
        plt.xlabel("Author")
        plt.ylabel("Number of Books")
        plt.xticks(rotation=45, ha="right")
        plt.legend()

        # Step 4: Adjust spacing and show the graph.
        plt.tight_layout()
        plt.show()
