import os
from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
from src.task4.merge_files import join_squad_possession_shooting
from src.task4.data_wrangling import clean_and_verify_sot_data
from src.task4.data_preparation import categorize_possession_and_sample
from src.task4.descriptive_statistics import generate_sot_descriptive_summary
from src.task4.confidence_interval import compute_sot_confidence_interval
from src.task4.two_sample_t_test import execute_possession_sot_ttest

def main():
    raw_std = project_root / 'data' / 'raw' / 'task4' / 'squad_standard.csv'
    raw_shoot = project_root / 'data' / 'raw' / 'task4' / 'squad_shooting.csv'
    processed_file = project_root / 'data' / 'processed' / 'task4' / 'task4_sampled_data.csv'

    boxplot_out = project_root / 'figures' / 'task4' / 'boxplot_sot.png'
    hist_out = project_root / 'figures' / 'task4' / 'histogram_sot.png'
    ci_plot_out = project_root / 'figures' / 'task4' / 't_distribution_task4.png'

    os.makedirs(project_root / 'data' / 'processed' / 'task4', exist_ok=True)
    os.makedirs(project_root / 'figures' / 'task4', exist_ok=True)

    # 1. Merge Files
    df_merged = join_squad_possession_shooting(raw_std, raw_shoot)

    # 2. Data Wrangling
    df_wrangled = clean_and_verify_sot_data(df_merged)

    # 3. Data Preparation & Sampling (Strictly 40 records)
    df_prepared = categorize_possession_and_sample(df_wrangled, sample_size=40)
    df_prepared.to_csv(processed_file, index=False)
    print(f"[✔] Saved sampled data (n={len(df_prepared)}) to {processed_file}\n")

    # 4. Descriptive Statistics & Outliers
    stats, outliers = generate_sot_descriptive_summary(df_prepared, boxplot_out, hist_out)
    print("--- Descriptive Statistics (SoT%) ---")
    print(stats)
    
    print("\n--- Detected Outliers (IQR Method) ---")
    if not outliers.empty:
        print(outliers[['Squad', 'Possession_Style', 'SoT%']])
    else:
        print("No mathematical outliers detected.")

    # 5. Confidence Interval
    mean, ci_lower, ci_upper = compute_sot_confidence_interval(df_prepared, ci_plot_out)
    print(f"\n--- 95% Confidence Interval ---")
    print(f"Sample Mean: {mean:.2f}%")
    print(f"95% CI: [{ci_lower:.2f}%, {ci_upper:.2f}%]")

    # 6. Inferential Statistics (Two-Sample t-Test)
    t_stat, p_val, mean_high, mean_low = execute_possession_sot_ttest(df_prepared)
    print(f"\n--- Welch's Two-Sample t-Test ---")
    print(f"High Possession Mean SoT%: {mean_high:.2f}%")
    print(f"Low/Mid Possession Mean SoT%: {mean_low:.2f}%")
    print(f"t-statistic: {t_stat:.4f}")
    print(f"p-value: {p_val:.4f}")
    
    print("\n--- Final Answer ---")
    if p_val < 0.05:
        if mean_high > mean_low:
            print("Yes. Teams with >55% possession have a significantly higher SoT%. Reject H0.")
        else:
            print("No. Teams with >55% possession actually have a significantly LOWER SoT%. Reject H0.")
    else:
        print("No. There is no statistically significant difference in SoT% between the two groups. Fail to reject H0.")

if __name__ == '__main__':
    main()