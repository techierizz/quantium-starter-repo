import pandas as pd
import os

# Define the path to the data folder
base_path = os.path.dirname(os.path.abspath(__file__)) 
data_folder = os.path.join(base_path, 'data')
output_file = os.path.join(base_path, 'formatted_data.csv')

# List to hold dataframes
dfs = []

# 1. Iterate through the files in the data folder
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(data_folder, filename)
        df = pd.read_csv(file_path)
        
        # 2. Filter for "Pink Morsel" only
        # df = df[df['product'] == 'pink morsel']
        df = df[df['product'].str.lower() == 'pink morsel']
        
        # 3. Calculate Sales (quantity * price)
        # We strip the '$' from price and convert to float first
        df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
        df['sales'] = df['quantity'] * df['price']
        
        # 4. Keep only the necessary columns
        df = df[['sales', 'date', 'region']]
        
        dfs.append(df)

# 5. Combine all three files into one
final_df = pd.concat(dfs, ignore_index=True)

# 6. Save to a single CSV
final_df.to_csv(output_file, index=False)

print(f"Success! Processed data saved to {output_file}")