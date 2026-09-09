import scipy.stats as stats

def run_t_test(df):
    defensive_data = df[df['Tactical_Role'] == 'Defensive']['TklW_per_90'].dropna()
    attacking_data = df[df['Tactical_Role'] == 'Attacking']['TklW_per_90'].dropna()

    # Welch's t-test (equal_var=False handles groups with potentially different variances)
    t_stat, p_value = stats.ttest_ind(defensive_data, attacking_data, equal_var=False)

    return t_stat, p_value