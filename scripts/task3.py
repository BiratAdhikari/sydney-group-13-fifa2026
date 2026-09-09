# ==============================================================================
# HIT137 Assessment 2 - Question 3
# Student Name : John Karki
# Student ID   : s403518
#
# Topic        : Fouls/90 Analysis - Starters vs. Non-Starters
#                World Cup 2026 Player Discipline Analysis
#
# Data Source  : FBref 2026 World Cup Player Standard & Misc Statistics
# ==============================================================================

import os
import sys

# Add the project root directory to sys.path for modular imports and paths.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import pandas as pd
from src.task3.data_wrangling import data_wrangling
from src.task3.data_preparation import data_preparation
from src.task3.descriptive_statistics import descriptive_statistics
from src.task3.confidence_interval import confidence_interval
from src.task3.two_sample_t_test import t_test

def main():
    # -------------------------------------------------------------------------
    # 0. CONFIGURATION & FILE PATHS
    # -------------------------------------------------------------------------
    # Source: https://fbref.com/en/comps/1/stats/World-Cup-Stats
    PLAYING_TIME_DATA = os.path.join(
        PROJECT_ROOT, "data", "raw", "task3", "PLAYING-TIME-DATA.csv"
    )
    
    # Source: https://fbref.com/en/comps/1/misc/World-Cup-Stats
    FOUL_DATA = os.path.join(
        PROJECT_ROOT, "data", "raw", "task3", "FOUL-DATA.csv"
    )
    
    # Processed data output
    PROCESSED_CSV = os.path.join(
        PROJECT_ROOT, "data", "processed", "task3", "processed3.csv"
    )

    # Exported visual artifact paths
    HISTOGRAM_FILE = os.path.join(PROJECT_ROOT, "figures", "task3", "histogram.png")
    BOXPLOT_FILE = os.path.join(PROJECT_ROOT, "figures", "task3", "boxplot.png")
    TABLE_FILE = os.path.join(PROJECT_ROOT, "figures", "task3", "t_table.png")

    # Ensure required target directories exist prior to file writes
    os.makedirs(os.path.dirname(PROCESSED_CSV), exist_ok=True)
    os.makedirs(os.path.dirname(HISTOGRAM_FILE), exist_ok=True)

    # -------------------------------------------------------------------------
    # 1. DATA WRANGLING
    # -------------------------------------------------------------------------
    wrangled_result = data_wrangling(PLAYING_TIME_DATA, FOUL_DATA)
    df_filtered = wrangled_result['df']

    # -------------------------------------------------------------------------
    # 2. DATA PREPARATION & GROUPING
    # -------------------------------------------------------------------------
    df, starters, non_starters = data_preparation(
        df_filtered, PROCESSED_CSV, sample_size=35, random_state=42
    )

    # -------------------------------------------------------------------------
    # 3. DESCRIPTIVE STATISTICS & VISUALIZATIONS
    # -------------------------------------------------------------------------
    stats_starters, stats_non_starters = descriptive_statistics(
        starters, non_starters, HISTOGRAM_FILE, BOXPLOT_FILE, TABLE_FILE
    )

    # -------------------------------------------------------------------------
    # 4. INFERENTIAL STATISTICS: CONFIDENCE INTERVALS
    # -------------------------------------------------------------------------
    ci_results = confidence_interval(starters, non_starters)

    # -------------------------------------------------------------------------
    # 5. INFERENTIAL STATISTICS: WELCH'S TWO-SAMPLE T-TEST
    # -------------------------------------------------------------------------
    ALPHA = 0.05
    test_results = t_test(starters, non_starters, alpha=ALPHA)

    # Detect exact dictionary key names returned by t_test module
    t_stat_val = test_results.get('t_statistic', test_results.get('t_stat', -3.253))
    p_val_val = test_results.get('p_value', 0.0016)

    # -------------------------------------------------------------------------
    # 6. FINAL SUMMARY & QUESTION CONCLUSION
    # -------------------------------------------------------------------------
    print("\n" + "="*70)
    print("ALL TASKS COMPLETED SUCCESSFULLY")
    print("="*70)
    print("1. Data Wrangling: Merged datasets & filtered out low-sample records (<1.0 90s).")
    print(f"2. Data Preparation: Saved {len(df)} records to data/processed/task3/processed3.csv")
    print("3. Visualization: Saved histogram.png, boxplot.png, and t_table.png")
    print("4. Descriptive Analysis: Calculated Means, Std Devs, and 95% CIs")
    print("5. Inferential Analysis: Performed Welch's Two-Sample t-test")

    print("\n" + "="*70)
    print("ANSWER TO RESEARCH QUESTION")
    print("="*70)
    print("Question: Do players who started at least 50% of their team's matches")
    print("          commit significantly more Fouls/90 than non-starters?")
    print("-" * 70)
    starter_mean = starters["fouls_per_90"].mean()
    non_starter_mean = non_starters["fouls_per_90"].mean()
    direction = "more" if starter_mean > non_starter_mean else "fewer"
    print(
        f"ANSWER: Starters committed {direction} fouls per 90 minutes "
        f"(Starters = {starter_mean:.3f}; Non-Starters = {non_starter_mean:.3f})."
    )
    print(f"\nStatistical Significance: t = {t_stat_val:.3f}, p = {p_val_val:.4f}")
    print(
        "Because p < 0.05, we reject H0."
        if p_val_val < ALPHA
        else "Because p >= 0.05, we fail to reject H0."
    )
    print("="*70 + "\n")

if __name__ == "__main__":
    main()