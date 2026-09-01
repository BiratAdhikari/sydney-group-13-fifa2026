import math
import scipy.stats as st


def ci_mean(sample, conf_lvl=0.95):
    """Calculate a confidence interval for the population mean."""

    x_bar = sample.mean()
    s = sample.std(ddof=1)
    n = len(sample)

    alpha = 1 - conf_lvl

    z_score = st.norm.ppf(
        q=1 - alpha / 2
    )

    std_err = s / math.sqrt(n)

    mrg_err = z_score * std_err

    ci_low = x_bar - mrg_err
    ci_upp = x_bar + mrg_err

    return (
        x_bar,
        s,
        n,
        ci_low,
        ci_upp
    )
