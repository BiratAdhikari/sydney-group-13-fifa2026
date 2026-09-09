import pandas as pd

def join_squad_possession_shooting(standard_path, shooting_path):
    df_std = pd.read_csv(standard_path, skiprows=5)
    df_shoot = pd.read_csv(shooting_path, skiprows=5)

    # Clean the Squad column to ensure a clean merge (removing country codes if present)
    df_std['Squad'] = df_std['Squad'].str.replace(r'^[a-z]{2}\s', '', regex=True)
    df_shoot['Squad'] = df_shoot['Squad'].str.replace(r'^[a-z]{2}\s', '', regex=True)

    # Inner join on Squad
    df_merged = pd.merge(
        df_std[['Squad', 'Poss']], 
        df_shoot[['Squad', 'SoT%']], 
        on='Squad', 
        how='inner'
    )
    return df_merged