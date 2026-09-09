import pandas as pd

def categorize_possession_and_sample(df, sample_size=40, random_seed=42):
    def classify_possession(poss):
        if poss > 55.0:
            return 'High Possession (>55%)'
        else:
            return 'Low/Mid Possession (<=55%)'

    df['Possession_Style'] = df['Poss'].apply(classify_possession)

    # Strictly sample 40 records
    if len(df) > sample_size:
        df_sampled = df.sample(n=sample_size, random_state=random_seed)
    else:
        df_sampled = df.copy()

    return df_sampled