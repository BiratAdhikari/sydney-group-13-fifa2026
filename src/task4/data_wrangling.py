import pandas as pd

def clean_and_verify_sot_data(df_merged):
    # Drop rows with missing values
    df_cleaned = df_merged.dropna(subset=['Poss', 'SoT%']).copy()
    
    # Ensure columns are numeric
    df_cleaned['Poss'] = pd.to_numeric(df_cleaned['Poss'], errors='coerce')
    df_cleaned['SoT%'] = pd.to_numeric(df_cleaned['SoT%'], errors='coerce')
    
    # Drop any rows that became NaN after forced numeric conversion
    df_cleaned = df_cleaned.dropna().copy()

    return df_cleaned