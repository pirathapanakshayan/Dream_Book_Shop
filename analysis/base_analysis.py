from abc import ABC, abstractmethod


# Caption: Strategy Pattern starts here.
# BaseAnalysis is the common parent class for all analysis strategies.
# OOP - Inheritance: All analysis classes inherit from this base class.
# SOLID - LSP: Any child analysis class can be used wherever BaseAnalysis is expected.
# SOLID - ISP: The interface is small and only asks for analysis-related methods.
class BaseAnalysis(ABC):
    """Abstract OOP class for all analysis strategies."""

    @abstractmethod
    def get_result(self, data):
        """Step 1 in every strategy: calculate and return the analysis result."""
        pass

    @abstractmethod
    def show_table(self, result):
        """Step 2 in every strategy: display the result as a terminal table."""
        pass

    @abstractmethod
    def show_graph(self, result):
        """Step 3 in every strategy: display the result as a matplotlib graph."""
        pass

    def run(self, data):
        """Template method: run the same steps for every analysis strategy."""
        # Step 1: Get the result from the selected analysis class.
        result = self.get_result(data)

        # Step 2: Show the result table.
        self.show_table(result)

        # Step 3: Show the result graph.
        self.show_graph(result)

    def print_table(self, title, result):
        """Reusable helper function for printing pandas DataFrames neatly."""
        # Step 1: Print the table title.
        print(f"\n{title}")

        # Step 2: Print the DataFrame without row index numbers.
        print(result.to_string(index=False))
