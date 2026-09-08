import scipy.stats as stats
import numpy as np

def t_test(starters, non_starters, x1=None, x2=None, s1=None, s2=None, alpha=0.05):
    # Detect exact fouls column dynamically
    col = next((c for c in ['fouls_per_90', 'Fouls_90', 'Fls_90', 'Fls/90', 'Fouls/90'] if c in starters.columns), None)

    s1_series = starters[col].dropna()
    s2_series = non_starters[col].dropna()

    # Calculate exact sample parameters from series directly
    x1, x2 = s1_series.mean(), s2_series.mean()
    s1, s2 = s1_series.std(), s2_series.std()
    n1, n2 = len(s1_series), len(s2_series)

    # Welch's t-test calculation
    se_diff = np.sqrt((s1**2 / n1) + (s2**2 / n2))
    t_stat = (x1 - x2) / se_diff

    # Welch-Satterthwaite degrees of freedom formula
    welch_df = ((s1**2 / n1 + s2**2 / n2) ** 2) / (
        ((s1**2 / n1) ** 2 / (n1 - 1)) + ((s2**2 / n2) ** 2 / (n2 - 1))
    )

    p_val = stats.t.sf(np.abs(t_stat), df=welch_df) * 2
    decision = "Reject H0" if p_val < alpha else "Fail to Reject H0"

    print("\n============================================================")
    print("5. INFERENTIAL STATISTICS - TWO-SAMPLE T-TEST")
    print("============================================================")
    print(f"t-statistic: {t_stat:.3f}")
    print(f"Degrees of freedom: {welch_df:.3f}")
    print(f"p-value: {p_val:.4f}")
    print(f"Decision: {decision}")

    return {
        't_statistic': t_stat,
        'welch_df': welch_df,
        'p_value': p_val,
        'decision': decision
    }
