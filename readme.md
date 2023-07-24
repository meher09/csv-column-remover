# CSV Column Remover Script

This Python script removes specified columns from a CSV file. The user inputs the filename of the CSV file and the names of the columns to be removed. The script then removes these specified columns and writes the results to a new CSV file.

## Requirements

This script requires Python 3 and the pandas library. If you don't have pandas installed, you can install it using pip:

```shell
pip install pandas
```
## Usage

Follow the steps below to use the `csv_column_remover.py` script:

1. **Run the script:** 

    Open your command-line interface, navigate to the directory containing `csv_column_remover.py`, and execute the script with Python:
    ```bash
    python csv_column_remover.py
    ```

2. **Provide the CSV filename:** 

    Upon prompt, enter the filename (with its full path if not in the current directory) of the CSV file from which you wish to remove columns.

3. **Input the column names to remove:** 

    Next, when asked, provide a comma-separated list of column names that you want to remove from the CSV file.

The script will process your CSV file and generate a new file with the specified columns removed.

## Notes

- **Column Removal:** 

    If one or more specified column names do not exist in the CSV file, the script will show an error message for those columns but will continue to remove those that exist.

- **File Paths:** 

    Ensure to use the correct format for your operating system when providing the file paths. For instance, use backslashes (`\`) on Windows, and forward slashes (`/`) on UNIX-based systems like Linux or macOS.

- **Python and pandas:** 

    This script requires both Python and pandas to be installed on your system. If they aren't, install them first before running the script.
