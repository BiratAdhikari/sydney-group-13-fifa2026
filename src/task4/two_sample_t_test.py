import scipy.stats as stats

def execute_possession_sot_ttest(df):
    high_data = df[df['Possession_Style'] == 'High Possession (>55%)']['SoT%'].dropna()
    low_data = df[df['Possession_Style'] == 'Low/Mid Possession (<=55%)']['SoT%'].dropna()

    t_stat, p_value = stats.ttest_ind(high_data, low_data, equal_var=False)

    return t_stat, p_value, high_data.mean(), low_data.mean()