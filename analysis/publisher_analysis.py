import matplotlib.pyplot as plt

from analysis.base_analysis import BaseAnalysis


# Caption: Strategy Pattern - this is one concrete analysis strategy.
# OOP - Inheritance: This class inherits from BaseAnalysis.
# SOLID - SRP: This class only handles publisher analysis.
class PublisherAnalysis(BaseAnalysis):
    """Analysis class for counting books by publisher."""

    def __init__(self, top_limit=30):
        """Step by step: store how many top publishers should be shown."""
        # OOP - Encapsulation: top_limit is stored inside this object.
        self.top_limit = top_limit

    def get_top_limit(self):
        """Getter method for the top publisher limit."""
        return self.top_limit

    def set_top_limit(self, top_limit):
        """Setter method for the top publisher limit."""
        self.top_limit = top_limit

    def get_result(self, data):
        """Step by step: count books per publisher and keep the top publishers."""
        # Step 1: Group the DataFrame by publisher and count rows.
        publisher_counts = data.groupby("book publisher").size().sort_values(ascending=False)

        # Step 2: Keep only the top publishers so the graph is readable.
        result = publisher_counts.head(self.top_limit).reset_index(name="Number of Books")

        # Step 3: Rename the column for a clear table heading.
        result = result.rename(columns={"book publisher": "Publisher"})

        return result

    def show_table(self, result):
        """Step by step: show publisher counts as a terminal table."""
        # Step 1: Use the common print_table helper from BaseAnalysis.
        self.print_table("Number of Books Published by Publisher", result)

    def show_graph(self, result):
        """Step by step: show publisher counts as a line graph."""
        # Step 1: Create the graph area.
        plt.figure(figsize=(16, 6))

        # Step 2: Draw a line graph with publishers on the x-axis.
        plt.plot(result["Publisher"], result["Number of Books"], marker="o")

        # Step 3: Add title, axis labels, rotated x labels, and grid.
        plt.title("Number of Books Published by Publisher")
        plt.xlabel("Publisher")
        plt.ylabel("Number of Books")
        plt.xticks(rotation=65, ha="right")
        plt.grid(True, alpha=0.35)

        # Step 4: Adjust spacing and show the graph.
        plt.tight_layout()
        plt.show()
