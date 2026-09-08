import pandas as pd
# Sample size for random sampling
# Random seed for uniformreproducibility
SAMPLE_SIZE = 40    
def prepare_data(df, sample_size=SAMPLE_SIZE, random_seed=9):

    # TKLW means Tackles Won, and 90s means the number of 90-minute intervals played. We calculate Tackles Won per 90 minutes.
    df['TklW_per_90'] = df['TklW'] / df['90s']

    # Classify into player Roles
    def classify_role(pos):
        if pos in ['GK', 'DF']:
            return 'Defensive'
        elif pos in ['MF', 'FW']:
            return 'Attacking'
        return 'Other'

    df['Tactical_Role'] = df['Primary_Pos'].apply(classify_role)
    
    # Filter out any unexpected/unmapped positions
    df = df[df['Tactical_Role'] != 'Other']

    # Random Sampling from the full tournament population (Restricted to 40 records)
    if len(df) > sample_size:
        df_sampled = df.sample(n=sample_size, random_state=random_seed)
    else:
        df_sampled = df.copy()

    print(f"Sampled DataFrame shape: {df_sampled.shape}")
    print(df_sampled.to_string(index=False))
    return df_sampled