import os
from pathlib import Path
import sys

# Ensure Python can find the src modules from the root director
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.defenderVsMidfielderTask2.twoSample_t_Test import run_t_test
from src.defenderVsMidfielderTask2.confidenceInterval import calculate_confidence_interval
from src.defenderVsMidfielderTask2.descriptiveAndStatistics import get_descriptive_stats
from src.defenderVsMidfielderTask2.dataPreparation import prepare_data
from src.defenderVsMidfielderTask2.dataWrangling import wrangle_data
def main():

    raw_standard = project_root / 'data' / 'raw' / 'task2DefenderVsMidfielderRaw' / 'standardStats_Raw.csv'
    raw_miscellaneous = project_root / 'data' / 'raw' / 'task2DefenderVsMidfielderRaw' / 'miscellaneousStats_Raw.csv'
    processed_file = project_root / 'data' / 'processed' / 'task2DefenderVsMidfielderProcessed' / 'finalSample_Processed.csv'

    boxplot_out = project_root / 'figures' / 'task2DefenderVsMidfielderFigures' / 'boxplot_tackles.png'
    hist_out = project_root / 'figures' / 'task2DefenderVsMidfielderFigures' / 'histogram_tackles.png'
    ci_plot_out = project_root / 'figures' / 'task2DefenderVsMidfielderFigures' / 't_distribution.png'

    print(f"Raw standard data path: {raw_standard}")
    print(f"Raw miscellaneous data path: {raw_miscellaneous}")
    

    # 1. Data Wrangling
    df_wrangled = wrangle_data(raw_standard, raw_miscellaneous)

    # 2. Data Preparation & Sampling (Strictly 40 records)
    df_prepared = prepare_data(df_wrangled, sample_size=40)
    df_prepared.to_csv(processed_file, index=False)
    print(f"Saved sampled data (n={len(df_prepared)}) to {processed_file}\n")

    # 3. Descriptive Statistics & Outliers
    stats, outliers = get_descriptive_stats(df_prepared, boxplot_out, hist_out)
    print("--- Descriptive Statistics (Tackles/90) ---")
    print(stats)
    
    print("\n--- Detected Outliers (IQR Method) ---")
    if not outliers.empty:
        print(outliers[['Player', 'Squad', 'Tactical_Role', 'TklW_per_90']])
    else:
        print("No mathematical outliers detected.")

    # 4. Confidence Interval
    mean, ci_lower, ci_upper = calculate_confidence_interval(df_prepared, ci_plot_out)
    print(f"\n--- 95% Confidence Interval ---")
    print(f"Sample Mean: {mean:.2f}")
    print(f"95% CI: [{ci_lower:.2f}, {ci_upper:.2f}]")

    # 5. Inferential Statistics (Two-Sample t-Test)
    t_stat, p_val = run_t_test(df_prepared)
    print(f"\n--- Welch's Two-Sample t-Test ---")
    print(f"t-statistic: {t_stat:.4f}")
    print(f"p-value: {p_val:.4f}")
    
    if p_val < 0.05:
        print("Conclusion: Reject H0. Defensive players win significantly more tackles per 90.")
    else:
        print("Conclusion: Fail to reject H0. No statistically significant difference found.")
    
if __name__ == "__main__":
    main()

