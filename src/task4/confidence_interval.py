import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def compute_sot_confidence_interval(df, plot_path, confidence_level=0.95):
    data = df['SoT%'].dropna()
    n = len(data)
    mean = np.mean(data)
    standard_error = stats.sem(data)

    t_crit = stats.t.ppf((1 + confidence_level) / 2., n - 1)
    margin_of_error = t_crit * standard_error
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error

    x = np.linspace(mean - 4*standard_error, mean + 4*standard_error, 200)
    y = stats.t.pdf(x, df=n-1, loc=mean, scale=standard_error)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f't-distribution (df={n-1})')
    plt.fill_between(x, y, where=(x >= lower_bound) & (x <= upper_bound), 
                     alpha=0.3, color='green', label=f'{int(confidence_level*100)}% CI')
    plt.axvline(mean, color='red', linestyle='--', label=f'Mean: {mean:.1f}%')
    plt.title('Confidence Interval for Mean Squad SoT%')
    plt.xlabel('Mean Shot on Target Percentage (%)')
    plt.ylabel('Density')
    plt.legend()
    plt.savefig(plot_path)
    plt.close()

    return mean, lower_bound, upper_bound