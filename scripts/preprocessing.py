import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# Caculate percentage of missing values in dataframe
def caculate_missing_percentage(dataframe):
    # Determine the total numer of element in dataframe
    total_elements = np.prod(dataframe.shape)
    
    # Calculate the total number of missing values in each column
    missing_values = dataframe.isna().sum()
    
    # Sum of the total numer of missing values 
    total_missing = missing_values.sum()

    # Compute the percentage of missing values 
    percentage_missing = (total_missing / total_elements) * 100 

    # Print the result, rounded to two decimal 
    print(f"The dataset has {round(percentage_missing, 2)}% missing values.")

# Check missing values
def check_missing_values(df):
    """check missing values in the dataset."""
    missing_values = df.isnull().sum()
    missing_percentage = 100 * df.isnull().sum() / len(df)
    column_data_types = df.dtypes
    missing_table = pd.concat([missing_values, missing_percentage, column_data_types], axis=1,
                              keys=['Missing Values', 
                                    '% of Total Values',
                                    'Data Types'])
    return missing_table.sort_values('% of Total Values', ascending=False).round(2)

def outlier_box_plots(df):
    for column in df:
        plt.figure(figsize=(10,6))
        sns.boxplot(x=df[column])
        plt.title(f"Box plot of {column}")
        plt.show()


def drop_high_missing_columns(df, threshold=50):
    """
    Drop columns with missing values above the specified threshold.
    
    :param df: pandas DataFrame
    :param threshold: percentage threshold for dropping columns (default 50%)
    :return: DataFrame with high-missing columns dropped
    """
    missing_series = df.isnull().sum() / len(df) * 100
    columns_to_drop = missing_series[missing_series > threshold].index
    df_cleaned = df.drop(columns=columns_to_drop)
    print(f"Dropped columns: {list(columns_to_drop)}")
    return df_cleaned

def drop_high_missing_rows(df, threshold=50):
    """
    Drop rows with a high percentage of missing values.
    
    :param df: pandas DataFrame
    :param threshold: percentage threshold for dropping rows (default 50%)
    :return: DataFrame with high-missing rows dropped
    """
    numerical_columns = df.select_dtypes(include=['number']).columns
    
    missing_series = df[numerical_columns].isnull().sum(axis=1) * 100 / len(numerical_columns)
    rows_to_drop = missing_series[missing_series > threshold].index

    # Extract contry names of the rows to dropped
    dropped_countries = df.loc[rows_to_drop, 'Country Name'].tolist()

    df_cleaned = df.drop(rows_to_drop)

    print(f"Dropped Countries: {dropped_countries}")
    print(f"Dropped rows: {list(rows_to_drop)}")
    return df_cleaned