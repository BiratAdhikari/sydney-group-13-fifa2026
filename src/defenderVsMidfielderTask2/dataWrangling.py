import pandas as pd

def wrangle_data(standard_data_path, miscellaneous_data_path):

    # Data on the CSV files starting from the 6th row (index 5) to skip metadata
    df_standard = pd.read_csv(standard_data_path, skiprows=5)
    df_miscellaneous = pd.read_csv(miscellaneous_data_path, skiprows=5)

    df_finalized = pd.merge(
        df_standard[['Player', 'Squad', 'Pos']], 
        df_miscellaneous[['Player', 'Squad', '90s', 'TklW']], 
        on=['Player', 'Squad'], 
        how='inner'
    )

    print(df_finalized.head(10))
    
    # Remove players with 0 minutes to avoid division by zero errors
    df_finalized = df_finalized[df_finalized['90s'] > 0].copy()

    # Clean Pos column: Isolate the first 2 characters to assign a primary position
    df_finalized['Primary_Pos'] = df_finalized['Pos'].str[:2]

    return df_finalized