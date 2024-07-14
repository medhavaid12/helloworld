print("Hello, World!")

import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'your_file.xlsx'

# Load the Excel file
df = pd.read_excel(file_path)

# Display the first few rows of the dataframe to verify the data is loaded
print(df.head())