import pandas as pd

# Get the CSV filename and columns to remove from the user
filename = input("Enter the CSV filename: ")
columns_to_remove = input("Enter column names to remove, separated by a comma: ").split(',')

# Strip any leading or trailing whitespace from the column names
columns_to_remove = [column.strip() for column in columns_to_remove]

# Load the CSV file into a DataFrame
df = pd.read_csv(filename)

# Check if the columns exist in the dataframe
non_existing_columns = [column for column in columns_to_remove if column not in df.columns]

# If there are non-existing columns, show an error message and remove only existing ones
if non_existing_columns:
    print(f"Columns {', '.join(non_existing_columns)} do not exist in the file.")

# Remove existing columns
columns_to_remove = [column for column in columns_to_remove if column in df.columns]
df = df.drop(columns=columns_to_remove)

# Save the modified DataFrame to a new CSV file
df.to_csv('modified_file.csv', index=False)

print("Operation completed. Check 'modified_file.csv' for the result.")
