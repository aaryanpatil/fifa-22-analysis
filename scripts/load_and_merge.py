import pandas as pd
import os

# Folder where CSVs are
data_folder = '../data'

# FIFA files
fifa_files = {
    2017: 'fifa17.csv',
    2018: 'fifa18.csv',
    2019: 'fifa19.csv',
    2020: 'fifa20.csv',
    2021: 'fifa21.csv',
    2022: 'fifa22.csv'
}

# List to hold dataframes
dfs = []

for year, filename in fifa_files.items():
    filepath = os.path.join(data_folder, filename)
    df = pd.read_csv(filepath)
    df['Year'] = year  # Add year column
    dfs.append(df)

# Concatenate all years into one dataframe
fifa_all = pd.concat(dfs, ignore_index=True)

# Save merged file (optional)
output_path = '../output/fifa_merged.csv'
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # make output folder if not exists
fifa_all.to_csv(output_path, index=False)

print("Data loaded and merged successfully!")
