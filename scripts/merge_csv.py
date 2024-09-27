import pandas as pd
import os

def load_csv_files(csv_dir, csv_files):
    dataframes = []
    for file in csv_files:
        file_path = os.path.join(csv_dir, file)
        df = pd.read_csv(file_path)
        dataframes.append(df)
    return dataframes

def concat_dataframes(data_frames):
    return pd.concat(data_frames, axis=0, ignore_index=True)

def save_concat_dataframe(concat_df, output_file):
    concat_df.to_csv(output_file, index=False)
    print(f"Concat data saved to {output_file}")