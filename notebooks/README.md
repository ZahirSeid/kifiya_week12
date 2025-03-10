# Task 1: Data Cleaning from JSON Files

## Overview

In **Task 1**, we developed a data processing pipeline that performs the following operations:

1. **Convert JSON to DataFrame**: JSON files are read and converted into Pandas DataFrames.
2. **Data Cleaning**:
   - **Remove Duplicates**: Identifies and removes any duplicate rows from the dataset.
   - **Handle Missing Values**: Fills missing values using forward and backward filling techniques to ensure the integrity of the data.
   - **Date Conversion**: Columns that contain date-related information are converted into `datetime` objects for consistency.
3. **Data Export**:
   - The cleaned DataFrame is saved as a CSV file, making it easier for further analysis and reporting.
4. **Optional Database Storage**:
   - The cleaned data can also be optionally stored in a PostgreSQL database. The table is created or replaced with each process, and the data is stored efficiently for future querying.

## Process Flow

1. **Input**: JSON files located in a specified directory.
2. **Processing**:
   - Each JSON file is loaded into a DataFrame.
   - The DataFrame undergoes a series of cleaning steps: duplicates are removed, missing values are filled, and date columns are standardized.
3. **Output**:
   - The cleaned data is saved as a CSV file in a designated output folder.
   - Optionally, the cleaned data is stored in a PostgreSQL database for further use in analysis or reporting.

## Features

- **Data Conversion**: Efficiently converts JSON data to a format suitable for further processing.
- **Data Cleaning**: Handles common data issues such as missing values and duplicates.
- **Date Handling**: Automatically converts date columns to the appropriate format for analysis.
- **Logging**: Logs every step of the process, including successes, warnings, and errors, to ensure transparency and easy troubleshooting.
- **Database Integration**: Optionally stores cleaned data in a PostgreSQL database for easy querying and access.

## Log File

All operations are logged to a `logfile.log`, capturing:
- Success messages
- Warnings (e.g., empty DataFrames or missing values)
- Errors (e.g., issues with reading JSON files, or database connection issues)

This log ensures that each step of the cleaning process is tracked and allows for easy identification of any issues that might arise.

## Conclusion

Task 1 provides a comprehensive solution for cleaning and processing JSON data, making it ready for further use, whether that involves saving the data as a CSV file or storing it in a PostgreSQL database for further analysis. The pipeline is designed for scalability and transparency, with clear logging to help track its progress.

