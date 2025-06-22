import pandas as pd

# Step 1: Read the master and updates CSV files
try:
    master_df = pd.read_csv("PigsFlyPolls.csv", engine='python', encoding='utf-8-sig', delimiter=',')
    updates_df = pd.read_csv("PigsFlyPolls_updated.csv", engine='python', encoding='utf-8-sig', delimiter=',')
except Exception as e:
    print(f"Error reading CSV files: {e}")
    exit()

# Step 2: Check if the DataFrame has loaded correctly
print("Master DataFrame before any changes:")
print(master_df.head())

# Check the structure of the dataframe
print("Columns in master dataframe:", master_df.columns)

# Step 3: If CSV file is not separated correctly (i.e., one column), split it manually
if len(master_df.columns) == 1:
    master_df = master_df[master_df.columns[0]].str.split(',', expand=True)
    master_df.columns = ['Pollster', 'Yes', 'No', 'Undecided']

# Step 4: Check if the update CSV is in the correct format
if len(updates_df.columns) == 1:
    updates_df = updates_df[updates_df.columns[0]].str.split(',', expand=True)
    updates_df.columns = ['Pollster', 'Yes', 'No', 'Undecided']

# Step 5: Clean percentage strings and convert to numeric, skipping invalid rows
def clean_percentage(value):
    try:
        # Try to strip '%' and convert to float
        return float(value.strip().rstrip('%'))
    except ValueError:
        # If value is invalid (like 'Yes', 'No'), return a special value (e.g., 0 or any placeholder)
        return 0

# Apply the cleaning function to each column
for col in ['Yes', 'No', 'Undecided']:
    master_df[col] = master_df[col].apply(clean_percentage)
    updates_df[col] = updates_df[col].apply(clean_percentage)

# Step 6: Print cleaned dataframes
print("\nMaster DataFrame (After Cleaning):")
print(master_df.head())

print("\nUpdates DataFrame (After Cleaning):")
print(updates_df.head())

# Step 7: Merge updates into master, removing duplicates and keeping the latest records
updated_df = pd.concat([master_df, updates_df]).drop_duplicates(subset='Pollster', keep='last')

# Step 8: Sort the dataframe alphabetically by the 'Pollster' column
updated_df = updated_df.sort_values(by='Pollster')

# Step 9: Print the updated master dataframe
print("\nUpdated Master DataFrame (After Merging and Sorting):")
print(updated_df.head())

# Step 10: Write the updated dataframe to a new CSV file
updated_df.to_csv("PigsFlyPolls2.csv", index=False)
print("\nUpdated dataframe saved to PigsFlyPolls2.csv.")

# Step 11: Print the data types of the dataframe to confirm they're numeric
print("\nData types of the updated dataframe:")
print(updated_df.dtypes)

# Step 12: Calculate averages for 'Yes', 'No', and 'Undecided' columns
mean_yes = updated_df['Yes'].mean()
mean_no = updated_df['No'].mean()
mean_undecided = updated_df['Undecided'].mean()

# Step 13: Append averages as the last entry with 'Pollster' set to 'Average'
average_row = pd.DataFrame([{'Pollster': 'Average', 'Yes': mean_yes, 'No': mean_no, 'Undecided': mean_undecided}])
updated_df = pd.concat([updated_df, average_row], ignore_index=True)

# Step 14: Print the final updated dataframe with averages
print("\nFinal Updated DataFrame with Averages:")
print(updated_df)

# Step 15: Write the final dataframe to an Excel file
try:
    updated_df.to_excel("PigsFlyPolls.xlsx", index=False)
    print("\nExcel file saved successfully.")
except Exception as e:
    print(f"Error saving Excel file: {e}")
