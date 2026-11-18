# Dream Book Shop Data Analysis System Summary

## 1. System Overview

The Dream Book Shop Data Analysis System is a Python command-line application that analyses book dataset information from `books.csv`. The system loads the dataset, validates required columns, cleans missing or invalid values, and shows analysis results as terminal tables and Matplotlib graphs.

The main program file is:

```text
Dream_Book_Shop.py
```

The system is designed using Object-Oriented Programming concepts, SOLID principles, the Strategy Pattern, the Factory Method Pattern, and the Template Method Pattern.

## 2. Main Objectives

- Load book data from CSV or Excel files.
- Validate that all required dataset columns are available.
- Clean missing author, language, publisher, and publication year values.
- Analyse book publication data using different analysis classes.
- Show results in table format.
- Show results in graph format.
- Provide a simple menu-based CLI for user interaction.

## 3. Dataset

The default dataset file is:

```text
books.csv
```

Required columns:

```text
book
author
publication date
language
book publisher
ISBN
BNB id
```

These columns are checked by `ColumnValidator`.

## 4. Menu Options

The CLI menu contains these options:

```text
1. Publication Trends Over Time
2. Top 5 Most Prolific Authors
3. Language Distribution of Books
4. Number of Books Published by Publisher
5. Missing ISBN Analysis
6. Books Published Per Year Categorised by Language
7. Show all graphs
8. Exit
```

## 5. System Flow

1. The program starts from `Dream_Book_Shop.py`.
2. The default dataset file `books.csv` is selected.
3. `DataLoader` loads the dataset.
4. `ColumnValidator` checks required columns.
5. `DataCleaner` fills missing values and extracts publication years.
6. The menu is displayed to the user.
7. The user selects an analysis option.
8. `AnalysisFactory` creates the correct analysis object.
9. The selected analysis class calculates the result.
10. The result is printed as a table.
11. The result is displayed as a graph.
12. The menu repeats until the user selects exit.

## 6. Main Files and Responsibilities

### Dream_Book_Shop.py

This is the main CLI controller file.

Responsibilities:

- Starts the program.
- Defines the menu options.
- Loads, validates, and cleans the dataset.
- Shows the CLI menu.
- Receives user input.
- Runs the selected analysis.
- Handles invalid menu options.
- Handles keyboard interruption cleanly.

Important functions:

```python
load_validate_and_clean_data(file_name)
clean_file_name(file_name)
show_menu()
run_all_analyses(data)
main()
```

### data_loader.py

This file contains the `DataLoader` class.

Responsibility:

- Load CSV, XLSX, or XLS dataset files using pandas.

Main method:

```python
load_data(file_path)
```

### column_validator.py

This file contains the `ColumnValidator` class.

Responsibility:

- Check whether all required dataset columns exist.

Main method:

```python
validate(data)
```

### data_cleaner.py

This file contains the `DataCleaner` class.

Responsibilities:

- Fill missing authors with `Unknown Author`.
- Fill missing languages with `Unknown Language`.
- Fill missing publishers with `Unknown Publisher`.
- Extract publication year from publication date.
- Remove rows without valid publication year.

Main methods:

```python
clean_data(data)
_fill_missing_text(data, column_name, replacement_text)
_extract_year(value)
```

### analysis_factory.py

This file contains the `AnalysisFactory` class.

Responsibility:

- Create the correct analysis object based on the user's menu choice.

Main method:

```python
create_analysis(choice)
```

## 7. Analysis Classes

All analysis classes inherit from `BaseAnalysis`.

### BaseAnalysis

File:

```text
analysis/base_analysis.py
```

Purpose:

- Defines the common structure for all analysis classes.
- Uses abstract methods.
- Provides a reusable `run()` method.
- Provides a reusable `print_table()` method.

Important methods:

```python
get_result(data)
show_table(result)
show_graph(result)
run(data)
print_table(title, result)
```

### PublicationTrendsAnalysis

File:

```text
analysis/publication_trends_analysis.py
```

Purpose:

- Counts how many books were published in each year.
- Shows a line graph.
- X-axis shows every year without skipping years.

Output columns:

```text
Year
Number of Books
```

### TopAuthorsAnalysis

File:

```text
analysis/top_authors_analysis.py
```

Purpose:

- Finds the top 5 most prolific authors.
- Shows a bar chart.

Output columns:

```text
Author
Number of Books
```

### LanguageDistributionAnalysis

File:

```text
analysis/language_distribution_analysis.py
```

Purpose:

- Counts books by language.
- Shows a language distribution bar chart.

Output columns:

```text
Language
Number of Books
```

### PublisherAnalysis

File:

```text
analysis/publisher_analysis.py
```

Purpose:

- Counts books by publisher.
- Shows the top 30 publishers.
- Displays the graph as a line graph with markers.

Output columns:

```text
Publisher
Number of Books
```

Getter and setter methods:

```python
get_top_limit()
set_top_limit(top_limit)
```

### MissingIsbnAnalysis

File:

```text
analysis/missing_isbn_analysis.py
```

Purpose:

- Counts books with ISBN and without ISBN.
- Calculates percentage values.
- Shows the result as a graph.

Output columns:

```text
ISBN Status
Number of Books
Percentage
```

### YearLanguageAnalysis

File:

```text
analysis/year_language_analysis.py
```

Purpose:

- Counts books published per year by language.
- Uses the top 10 languages.
- Shows a multi-line graph.
- Places the graph legend outside the plot area for readability.

Output columns:

```text
Year
Language
Number of Books
```

## 8. Object Creation

Objects are created in these places:

### In Dream_Book_Shop.py

```python
loader = DataLoader()
validator = ColumnValidator()
cleaner = DataCleaner()
```

These objects are used for loading, validating, and cleaning the dataset.

### In analysis_factory.py

```python
return analysis_class()
```

This creates the selected analysis object.

Examples:

```text
Choice 1 -> PublicationTrendsAnalysis object
Choice 2 -> TopAuthorsAnalysis object
Choice 3 -> LanguageDistributionAnalysis object
Choice 4 -> PublisherAnalysis object
Choice 5 -> MissingIsbnAnalysis object
Choice 6 -> YearLanguageAnalysis object
```

### In Dream_Book_Shop.py menu logic

```python
analysis = AnalysisFactory.create_analysis(choice)
```

This receives the object created by the factory and calls:

```python
analysis.run(data)
```

## 9. OOP Concepts Used

### Class and Object

The system uses classes such as:

```text
DataLoader
ColumnValidator
DataCleaner
AnalysisFactory
BaseAnalysis
PublicationTrendsAnalysis
TopAuthorsAnalysis
LanguageDistributionAnalysis
PublisherAnalysis
MissingIsbnAnalysis
YearLanguageAnalysis
```

Objects are created from these classes to perform system tasks.

### Inheritance

All analysis classes inherit from `BaseAnalysis`.

Example:

```python
class PublisherAnalysis(BaseAnalysis):
```

### Abstraction

`BaseAnalysis` is an abstract class. It defines common methods that child classes must implement:

```python
get_result(data)
show_table(result)
show_graph(result)
```

### Encapsulation

`PublisherAnalysis` stores `top_limit` inside the object:

```python
self.top_limit = top_limit
```

Getter and setter methods are provided:

```python
get_top_limit()
set_top_limit(top_limit)
```

### Polymorphism

Every analysis class has the same method names:

```python
get_result()
show_table()
show_graph()
```

The main program can call:

```python
analysis.run(data)
```

without knowing the exact analysis class type.

## 10. Design Patterns Used

### Strategy Pattern

Each analysis is written as a separate strategy class:

```text
PublicationTrendsAnalysis
TopAuthorsAnalysis
LanguageDistributionAnalysis
PublisherAnalysis
MissingIsbnAnalysis
YearLanguageAnalysis
```

The user selects the strategy through the menu.

### Factory Method Pattern

`AnalysisFactory` creates the correct analysis object based on the user choice.

Example:

```python
analysis = AnalysisFactory.create_analysis(choice)
```

### Template Method Pattern

`BaseAnalysis.run()` defines the common execution steps:

```text
1. get_result()
2. show_table()
3. show_graph()
```

Every child analysis class follows this same structure.

## 11. SOLID Principles Used

### Single Responsibility Principle

Each class has one main responsibility:

```text
DataLoader -> loads data
ColumnValidator -> validates columns
DataCleaner -> cleans data
AnalysisFactory -> creates analysis objects
Analysis classes -> perform one analysis each
```

### Open/Closed Principle

New analysis types can be added by creating a new analysis class and updating the factory mapping.

### Liskov Substitution Principle

All child analysis classes can be used wherever `BaseAnalysis` is expected.

### Interface Segregation Principle

`BaseAnalysis` provides a small interface with only analysis-related methods.

### Dependency Inversion Principle

The main program depends on `AnalysisFactory` and `BaseAnalysis` behavior instead of directly depending on every analysis implementation.

## 12. Data Structures Used

### List

Used for required columns:

```python
REQUIRED_COLUMNS = [...]
```

### Dictionary

Used for menu options:

```python
MENU_OPTIONS = {...}
```

Also used in `AnalysisFactory` to map menu choices to classes:

```python
analysis_map = {...}
```

### Pandas DataFrame

Used to store and process dataset data.

### Pandas Series

Used for value counts and grouped analysis results.

## 13. Graphs Produced

The system produces these graphs:

```text
Publication Trends Over Time
Top 5 Most Prolific Authors
Language Distribution of Books
Number of Books Published by Publisher
Missing ISBN Analysis
Books Published Per Year Categorised by Language
```

Graph library:

```text
Matplotlib
```

## 14. Testing

The system includes automated tests inside the `tests` folder.

Test areas:

```text
Publication trends
Top authors
Language distribution
Publisher analysis
Missing ISBN analysis
Year-language analysis
CSV and Excel loading
Required column validation
Data cleaning
CLI menu options
```

The latest verified test result:

```text
22 tests passed
```

## 15. How to Run

From the `DreamBookAnalysisSystem` folder:

```bash
python Dream_Book_Shop.py
```

Using the project virtual environment from the outer project folder:

```bash
.venv\Scripts\python.exe DreamBookAnalysisSystem\Dream_Book_Shop.py
```

## 16. Conclusion

The Dream Book Shop Data Analysis System is a complete OOP-based Python data analysis system. It separates loading, validation, cleaning, object creation, and analysis into different classes. It uses pandas for data processing and Matplotlib for graph generation. The system follows important OOP concepts, design patterns, SOLID principles, and includes automated tests to verify the main features.
