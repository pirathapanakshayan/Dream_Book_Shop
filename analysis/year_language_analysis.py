import matplotlib.pyplot as plt

from analysis.base_analysis import BaseAnalysis


TOP_LANGUAGE_LIMIT = 10


# Caption: Strategy Pattern - this is one concrete analysis strategy.
# OOP - Inheritance: This class inherits from BaseAnalysis.
# SOLID - SRP: This class only handles year and language analysis.
class YearLanguageAnalysis(BaseAnalysis):
    """Analysis class for books published per year by language."""

    def get_result(self, data):
        """Step by step: count books per year for the top 10 languages."""
        # Step 1: Find the top 10 languages by total book count.
        top_languages = data["language"].value_counts().head(TOP_LANGUAGE_LIMIT).index

        # Step 2: Keep only rows that belong to the top 10 languages.
        filtered_data = data[data["language"].isin(top_languages)]

        # Step 3: Group by publication year and language, then count rows.
        result = (
            filtered_data.groupby(["publication_year", "language"])
            .size()
            .reset_index(name="Number of Books")
        )

        # Step 4: Rename columns for clear table headings.
        result = result.rename(
            columns={"publication_year": "Year", "language": "Language"}
        )

        # Step 5: Sort the result by year and language.
        result = result.sort_values(["Year", "Language"]).reset_index(drop=True)

        return result

    def show_table(self, result):
        """Step by step: show year-language analysis as a terminal table."""
        # Step 1: Use the common print_table helper from BaseAnalysis.
        self.print_table("Books Published Per Year Categorised by Language", result)

    def show_graph(self, result):
        """Step by step: show books per year by language as a multi-line graph."""
        # Step 1: Convert the table into a pivot table for line plotting.
        pivot_table = result.pivot(
            index="Year", columns="Language", values="Number of Books"
        ).fillna(0)

        # Step 2: Create the graph area.
        plt.figure(figsize=(14, 7))

        # Step 3: Draw one line for each language.
        for language in pivot_table.columns:
            plt.plot(
                pivot_table.index,
                pivot_table[language],
                marker="o",
                label=language,
            )

        # Step 4: Add title, axis labels, legend, and grid.
        plt.title("Books Published Per Year Categorised by Language")
        plt.xlabel("Year")
        plt.ylabel("Number of Books")
        plt.xticks(pivot_table.index.astype(int))
        plt.legend(title="Language", bbox_to_anchor=(1.02, 1), loc="upper left")
        plt.grid(True)

        # Step 5: Adjust spacing and show the graph.
        plt.tight_layout()
        plt.show()
