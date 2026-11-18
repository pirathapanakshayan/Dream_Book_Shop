from analysis_factory import AnalysisFactory
from column_validator import ColumnValidator
from data_cleaner import DataCleaner
from data_loader import DataLoader


# Caption: The program loads this dataset automatically when main.py runs.
DEFAULT_DATASET_FILE = "books.csv"


# Caption: Dictionary data structure is used for CLI menu options.
MENU_OPTIONS = {
    "1": "Publication Trends Over Time",
    "2": "Top 5 Most Prolific Authors",
    "3": "Language Distribution of Books",
    "4": "Number of Books Published by Publisher",
    "5": "Missing ISBN Analysis",
    "6": "Books Published Per Year Categorised by Language",
    "7": "Show all graphs",
    "8": "Exit",
}


def load_validate_and_clean_data(file_name):
    """Step by step: load, validate, and clean the dataset before analysis."""
    # SOLID - SRP: DataLoader only loads data.
    loader = DataLoader()

    # SOLID - SRP: ColumnValidator only validates required columns.
    validator = ColumnValidator()

    # SOLID - SRP: DataCleaner only cleans data.
    cleaner = DataCleaner()

    # Step 1: Load CSV or Excel data.
    data = loader.load_data(file_name)

    # Step 2: Check that all required columns exist.
    validator.validate(data)

    # Step 3: Clean missing values and create publication_year.
    cleaned_data = cleaner.clean_data(data)

    return cleaned_data


def clean_file_name(file_name):
    """Step by step: clean the file name entered by the user."""
    # Step 1: Remove spaces from the start and end.
    cleaned_name = file_name.strip()

    # Step 2: Remove hidden characters that sometimes appear in Windows input.
    cleaned_name = cleaned_name.lstrip("\ufeff")
    cleaned_name = cleaned_name.removeprefix(chr(239) + chr(187) + chr(191))

    # Step 3: Remove quotes if the user pasted a quoted file path.
    cleaned_name = cleaned_name.strip().strip('"').strip("'")

    return cleaned_name


def show_menu():
    """Step by step: print the CLI menu options."""
    # Step 1: Print the menu title.
    print("\nDream Book Shop Analysis Menu")

    # Step 2: Print each menu number and title from the dictionary.
    for number, title in MENU_OPTIONS.items():
        print(f"{number}. {title}")


def run_all_analyses(data):
    """Step by step: run every analysis strategy one by one."""
    # SOLID - LSP: Every analysis object can be used in the same way with run().
    for choice in ["1", "2", "3", "4", "5", "6"]:
        # Factory Method Pattern: The factory creates the correct analysis object.
        analysis = AnalysisFactory.create_analysis(choice)

        # Strategy Pattern: Different analysis objects use the same run() method.
        analysis.run(data)


def main():
    """Main CLI function that controls the program flow."""
    # SOLID - SRP: main.py controls CLI flow only.
    print("Dream Book Shop Data Analysis System")

    # Step 1: Use the default dataset file, so the menu opens straight away.
    file_name = DEFAULT_DATASET_FILE

    # Step 2: Load, validate, and clean the dataset.
    try:
        data = load_validate_and_clean_data(file_name)
    except FileNotFoundError as error:
        print(f"\nError: {error}")
        return
    except ValueError as error:
        print(f"\nError: {error}")
        return

    # Step 3: Keep showing the menu until the user exits.
    while True:
        show_menu()
        try:
            choice = clean_file_name(input("\nEnter your choice: "))
        except KeyboardInterrupt:
            print("\nProgram stopped by user.")
            break

        # Step 4: Exit when the user chooses option 8.
        if choice == "8":
            print("Thank you for using Dream Book Shop Data Analysis System.")
            break

        # Step 5: Run all graphs when the user chooses option 7.
        if choice == "7":
            run_all_analyses(data)
            continue

        # Step 6: Ask the factory for the selected analysis object.
        analysis = AnalysisFactory.create_analysis(choice)

        # Step 7: Show a friendly message for invalid choices.
        if analysis is None:
            print("Invalid option. Please enter a number from 1 to 8.")
            continue

        # Step 8: Run the selected analysis strategy.
        analysis.run(data)


if __name__ == "__main__":
    # This starts the CLI program when main.py is run directly.
    main()
