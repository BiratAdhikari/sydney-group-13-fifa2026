import math
import scipy.stats as st


def ci_mean(sample, conf_lvl=0.95):
    """
    Calculate a confidence interval for a population mean using t-distribution.
    Returns: (mean, std_dev, n, ci_lower, ci_upper)
    """
    x_bar = sample.mean()
    s = sample.std(ddof=1)
    n = len(sample)
    df = n - 1

    alpha = 1 - conf_lvl
    t_score = st.t.ppf(1 - alpha / 2, df)

    std_err = s / math.sqrt(n)
    margin_err = t_score * std_err

    ci_low = x_bar - margin_err
    ci_upp = x_bar + margin_err

    return x_bar, s, n, ci_low, ci_upp
