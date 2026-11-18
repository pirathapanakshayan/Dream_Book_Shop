# Caption: Python list data structure is used to store all required column names.
REQUIRED_COLUMNS = [
    "book",
    "author",
    "publication date",
    "language",
    "book publisher",
    "ISBN",
    "BNB id",
]


# Caption: OOP is used here because ColumnValidator is a class.
# SOLID - SRP: This class only validates columns. It does not load or clean data.
class ColumnValidator:
    """OOP class for checking required dataset columns."""

    def validate(self, data):
        """Step by step: compare dataset columns with the required columns list."""
        # Step 1: Create an empty list to store missing columns.
        missing_columns = []

        # Step 2: Check each required column one by one.
        for column in REQUIRED_COLUMNS:
            if column not in data.columns:
                missing_columns.append(column)

        # Step 3: If columns are missing, show a clear error message.
        if missing_columns:
            missing_text = ", ".join(missing_columns)
            required_text = ", ".join(REQUIRED_COLUMNS)
            raise ValueError(
                f"Missing required column(s): {missing_text}. "
                f"Required columns are: {required_text}."
            )

        # Step 4: Return True when all required columns are available.
        return True
