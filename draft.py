import pandas as pd
import numpy as np

# Load Excel file from user input
#file_path = input("Enter the file path of the Excel file: ")
df = pd.read_csv('modified.csv', index_col=())
print(df)

# Transpose the columns into rows
df = df.T
print(df)

# Validate the data (Example validation: Check if all values are numeric)
if df.dtypes.apply(pd.api.types.is_numeric_dtype).all():
    # Convert the DataFrame to a numpy array
    data = df.values
    print("Data is valid and converted to numpy array:")
    print(data)

    # Save numpy array as Excel file
    save_path = "E:\modified.xlsx"
    new_df = pd.DataFrame(data, index=df.index, columns=df.columns)  # Create a new DataFrame with the same row names and column names
    new_df.to_excel(save_path, index=True)  # Save the new DataFrame as an Excel file with row names included
    print("Numpy array has been saved as an Excel file.")
else:
    print("Data is not valid. Please ensure all values are numeric.")