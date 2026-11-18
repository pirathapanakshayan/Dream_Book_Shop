import matplotlib.pyplot as plt

from analysis.base_analysis import BaseAnalysis


# Caption: Strategy Pattern - this is one concrete analysis strategy.
# OOP - Inheritance: This class inherits from BaseAnalysis.
# SOLID - SRP: This class only handles publication trends analysis.
class PublicationTrendsAnalysis(BaseAnalysis):
    """Analysis class for books published per year."""

    def get_result(self, data):
        """Step by step: count how many books were published in each year."""
        # Step 1: Group the DataFrame by publication_year and count rows.
        year_counts = data.groupby("publication_year").size().sort_index()

        # Step 2: Convert the pandas Series into a DataFrame.
        result = year_counts.reset_index(name="Number of Books")

        # Step 3: Rename the column for a clear table heading.
        result = result.rename(columns={"publication_year": "Year"})

        return result

    def show_table(self, result):
        """Step by step: show publication trends as a terminal table."""
        # Step 1: Use the common print_table helper from BaseAnalysis.
        self.print_table("Publication Trends Over Time", result)

    def show_graph(self, result):
        """Step by step: show publication trends as a line graph."""
        # Step 1: Create the graph area.
        plt.figure(figsize=(10, 6))

        # Step 2: Draw the line graph using Year and Number of Books.
        plt.plot(result["Year"], result["Number of Books"], marker="o", label="Books")

        # Step 3: Add title, axis labels, legend, and grid.
        plt.title("Publication Trends Over Time")
        plt.xlabel("Year")
        plt.ylabel("Number of Books")
        plt.xticks(result["Year"].astype(int))
        plt.legend()
        plt.grid(True)

        # Step 4: Adjust spacing and show the graph.
        plt.tight_layout()
        plt.show()
