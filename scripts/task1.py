# ==============================================================================
# HIT140 Assessment 2 - Question 1
# Student Name : Hemanta Adhikari
# Student ID   : s403355
#
# Topic        : Shots/90 Analysis - Attacking Players
#                Under 25 vs Age 28+
#
# Data Source  : FBref 2026 World Cup Player Shooting Statistics
# ==============================================================================

import os
import sys
import matplotlib.pyplot as plt


# Make project root available for src imports.
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.task1.data_wrangling import data_wrangling
from src.task1.data_preparation import data_preparation
from src.task1.descriptive_statistics import descriptive_statistics
from src.task1.confidence_interval import confidence_interval
from src.task1.two_sample_t_test import t_test


RAW_FILE = os.path.join(
    PROJECT_ROOT,
    "data",
    "raw",
    "task1",
    "raw1.csv"
)

FILTERED_FILE = os.path.join(
    PROJECT_ROOT,
    "data",
    "processed",
    "task1",
    "processed1.csv"
)

RESULTS_FILE = os.path.join(
    PROJECT_ROOT,
    "docs",
    "task1.md"
)

FIGURES_FOLDER = os.path.join(
    PROJECT_ROOT,
    "figures",
    "task1"
)

HISTOGRAM_FILE = os.path.join(
    FIGURES_FOLDER,
    "histogram.png"
)

BOXPLOT_FILE = os.path.join(
    FIGURES_FOLDER,
    "boxplot.png"
)

T_DISTRIBUTION_FILE = os.path.join(
    FIGURES_FOLDER,
    "t_distribution.png"
)

RANDOM_SEED = 137
TOTAL_SAMPLE_SIZE = 35
UNDER25_SAMPLE_SIZE = 10
AGE28PLUS_SAMPLE_SIZE = 25
ALPHA = 0.05


def main():

    os.makedirs(
        os.path.join(
            PROJECT_ROOT,
            "data",
            "processed",
            "task1"
        ),
        exist_ok=True
    )

    os.makedirs(
        os.path.join(
            PROJECT_ROOT,
            "docs"
        ),
        exist_ok=True
    )

    os.makedirs(
        FIGURES_FOLDER,
        exist_ok=True
    )

    # ==========================================================================
    # Question 1
    #
    # Is there a statistically significant difference in Shots/90 between
    # attacking players under 25 and attacking players aged 28+?
    # ==========================================================================

    print("=" * 60)
    print("1. DATA WRANGLING")
    print("=" * 60)

    # 1. Data wrangling
    wrangled = data_wrangling(RAW_FILE)

    # 2. Data preparation and sampling
    df, under25, age28plus = data_preparation(
        wrangled["under25_all"],
        wrangled["age28plus_all"],
        wrangled["original_records"],
        FILTERED_FILE,
        RANDOM_SEED,
        TOTAL_SAMPLE_SIZE,
        UNDER25_SAMPLE_SIZE,
        AGE28PLUS_SAMPLE_SIZE,
    )

    # 3. Descriptive statistics
    stats_u25, stats_28plus = descriptive_statistics(
        under25,
        age28plus,
        HISTOGRAM_FILE,
        BOXPLOT_FILE,
    )

    # 4. Confidence interval
    ci_results = confidence_interval(
        under25,
        age28plus,
    )

    # 5. Welch two-sample t-test
    test_results = t_test(
        under25,
        age28plus,
        ci_results["s1"],
        ci_results["n1"],
        ci_results["s2"],
        ci_results["n2"],
        ALPHA,
        T_DISTRIBUTION_FILE,
    )

    # Keep the original result-generation section in task1.py.
    mean_difference = (
        stats_u25["mean"]
        -
        stats_28plus["mean"]
    )

    histogram_md = "../figures/task1/histogram.png"
    boxplot_md = "../figures/task1/boxplot.png"
    t_distribution_md = "../figures/task1/t_distribution.png"

    with open(
        RESULTS_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        
        file.write(
            "<!--\n"
            "==============================================================================\n"
            "HIT140 Assessment 2 - Question 1\n"
            "Student Name : Hemanta Adhikari\n"
            "Student ID   : s403355\n\n"
            "Topic        : Shots/90 Analysis - Attacking Players\n"
            "               Under 25 vs. Age 28+\n"
            "               World Cup 2026 Attacking Shooting Analysis\n\n"
            "Data Source  : FBref 2026 World Cup Player Shooting Statistics\n"
            "Data Source Link  : https://fbref.com/en/comps/1/shooting/World-Cup-Stats\n"
            "==============================================================================\n"
            "-->\n\n"
        )

        file.write("# Question 1 Results\n\n")

        file.write("## Analytical Question\n\n")
        file.write(
            "> Is there a statistically significant difference "
            "in Shots/90 between attacking players under 25 "
            "and attacking players aged 28+?\n\n"
        )

        file.write("## Dataset\n\n")
        file.write(
            "The analysis uses FIFA World Cup 2026 player "
            "shooting statistics obtained from FBref.\n\n"
        )

        file.write("- Raw dataset: `data/raw/task1/raw1.csv`\n")
        file.write(
            f"- Original records: **{wrangled['original_records']}**\n"
        )
        file.write(
            f"- Records removed during cleaning: "
            f"**{wrangled['records_removed']}**\n"
        )
        file.write(
            f"- Attacking players identified: "
            f"**{len(wrangled['attackers'])}**\n\n"
        )

        file.write("## 1. Data Wrangling\n\n")
        file.write(
            "The raw FBref CSV was cleaned before analysis. "
            "The actual FBref table header was identified, "
            "invalid Age and Sh/90 values were removed, and "
            "the Squad field was cleaned.\n\n"
        )
        file.write(
            "An attacking player was operationally defined as "
            "a player whose FBref position contains `FW`. "
            "This includes `FW`, `FWMF` and `MFFW` positions.\n\n"
        )
        file.write(
            f"- Original records: **{wrangled['original_records']}**\n"
        )
        file.write(
            f"- Records removed during cleaning: "
            f"**{wrangled['records_removed']}**\n"
        )
        file.write(
            f"- Attacking players: **{len(wrangled['attackers'])}**\n"
        )
        file.write(
            f"- Under 25 available: **{len(wrangled['under25_all'])}**\n"
        )
        file.write(
            f"- Age 28+ available: **{len(wrangled['age28plus_all'])}**\n\n"
        )

        file.write("## 2. Data Preparation and Sampling\n\n")
        file.write("- Under 25 group: `Age < 25`\n")
        file.write("- Age 28+ group: `Age >= 28`\n")
        file.write("- Players aged 25, 26 and 27 were excluded.\n")
        file.write("- Sampling method: Random sampling.\n")
        file.write(f"- Fixed random seed: **{RANDOM_SEED}**\n")
        file.write(f"- Final sample size: **{len(df)}**\n")
        file.write(f"- Under 25 sample: **{len(under25)}**\n")
        file.write(f"- Age 28+ sample: **{len(age28plus)}**\n\n")
        file.write(
            "The processed dataset is saved as "
            "`data/processed/processed1.csv`.\n\n"
        )

        file.write("## 3. Descriptive Statistics\n\n")
        file.write("| Statistic | Under 25 | Age 28+ |\n")
        file.write("|---|---:|---:|\n")
        file.write(
            f"| Sample size | {stats_u25['n']} | "
            f"{stats_28plus['n']} |\n"
        )
        file.write(
            f"| Mean | {stats_u25['mean']:.3f} | "
            f"{stats_28plus['mean']:.3f} |\n"
        )
        file.write(
            f"| Median | {stats_u25['median']:.3f} | "
            f"{stats_28plus['median']:.3f} |\n"
        )
        file.write(
            f"| Minimum | {stats_u25['min']:.3f} | "
            f"{stats_28plus['min']:.3f} |\n"
        )
        file.write(
            f"| Maximum | {stats_u25['max']:.3f} | "
            f"{stats_28plus['max']:.3f} |\n"
        )
        file.write(
            f"| Range | {stats_u25['range']:.3f} | "
            f"{stats_28plus['range']:.3f} |\n"
        )
        file.write(
            f"| Variance | {stats_u25['variance']:.3f} | "
            f"{stats_28plus['variance']:.3f} |\n"
        )
        file.write(
            f"| Standard deviation | {stats_u25['std_dev']:.3f} | "
            f"{stats_28plus['std_dev']:.3f} |\n"
        )
        file.write(
            f"| Q1 | {stats_u25['q1']:.3f} | "
            f"{stats_28plus['q1']:.3f} |\n"
        )
        file.write(
            f"| Q3 | {stats_u25['q3']:.3f} | "
            f"{stats_28plus['q3']:.3f} |\n"
        )
        file.write(
            f"| IQR | {stats_u25['iqr']:.3f} | "
            f"{stats_28plus['iqr']:.3f} |\n\n"
        )

        file.write("## 4. 95% Confidence Interval\n\n")
        file.write(
            "| Age Group | Mean | Standard Deviation | "
            "n | 95% Confidence Interval |\n"
        )
        file.write("|---|---:|---:|---:|---|\n")
        file.write(
            f"| Under 25 | {ci_results['x_bar1']:.3f} | "
            f"{ci_results['s1']:.3f} | {ci_results['n1']} | "
            f"{ci_results['ci_low1']:.3f} to "
            f"{ci_results['ci_upp1']:.3f} |\n"
        )
        file.write(
            f"| Age 28+ | {ci_results['x_bar2']:.3f} | "
            f"{ci_results['s2']:.3f} | {ci_results['n2']} | "
            f"{ci_results['ci_low2']:.3f} to "
            f"{ci_results['ci_upp2']:.3f} |\n\n"
        )

        file.write("## 5. Welch Two-Sample t-Test\n\n")
        file.write("### Null Hypothesis (H0)\n\n")
        file.write(
            "There is no difference in mean Shots/90 between "
            "attacking players under 25 and attacking players "
            "aged 28+.\n\n"
        )

        file.write("### Alternative Hypothesis (H1)\n\n")
        file.write(
            "There is a difference in mean Shots/90 between "
            "attacking players under 25 and attacking players "
            "aged 28+.\n\n"
        )

        file.write(f"- Significance level: **α = {ALPHA}**\n")
        file.write(
            f"- t-statistic: **{test_results['t_statistic']:.3f}**\n"
        )
        file.write(
            f"- Degrees of freedom: **{test_results['welch_df']:.3f}**\n"
        )
        file.write(
            f"- p-value: **{test_results['p_value']:.4f}**\n"
        )
        file.write(
            f"- Decision: **{test_results['decision']}**\n\n"
        )

        file.write("## 6. Conclusion\n\n")
        file.write(f"{test_results['conclusion']}\n\n")
        file.write(
            f"The mean Shots/90 for Under 25 players was "
            f"**{stats_u25['mean']:.3f}**, while the mean for "
            f"Age 28+ players was "
            f"**{stats_28plus['mean']:.3f}**.\n\n"
        )
        file.write(
            f"The difference between the sample means was "
            f"**{mean_difference:.3f} Shots/90**.\n\n"
        )
        file.write(
            "Because the p-value is greater than 0.05, the null "
            "hypothesis is not rejected. This does not prove that "
            "the population means are exactly equal. It means that "
            "the sample does not provide sufficient evidence of a "
            "statistically significant difference.\n\n"
        )

        file.write("## 7. Visualisations\n\n")
        file.write("### Histogram\n\n")
        file.write(f"![Shots/90 Histogram]({histogram_md})\n\n")
        file.write("### Boxplot\n\n")
        file.write(f"![Shots/90 Boxplot]({boxplot_md})\n\n")
        file.write("### t-Distribution\n\n")
        file.write(
            f"![Shots/90 t-Distribution]({t_distribution_md})\n\n"
        )

        file.write("## 8. Output Files\n\n")
        file.write("- Raw dataset: `data/raw/raw1.csv`\n")
        file.write(
            "- Processed dataset: `data/processed/processed1.csv`\n"
        )
        file.write("- Analysis script: `scripts/task1.py`\n")
        file.write(
            "- Confidence interval function: "
            "`src/Utility.py`\n"
        )
        file.write("- Histogram: `figures/task1/histogram.png`\n")
        file.write("- Boxplot: `figures/task1/boxplot.png`\n")
        file.write(
            "- t-Distribution: `figures/task1/t_distribution.png`\n\n"
        )
        
        file.write("## 9. How to Run\n\n")
        file.write(
            "From the project root, run the script directly:\n\n"
        )
        file.write("```bash\n")
        file.write("python scripts/task1.py\n")
        file.write("```\n\n")
        file.write(
            "Or from inside the `scripts/` folder:\n\n"
        )
        file.write("```bash\n")
        file.write("cd scripts\n")
        file.write("python task1.py\n")
        file.write("```\n\n")


        file.write("## 10. Data Source\n\n")
        file.write(
            "FBref.com (Sports Reference), FIFA World Cup "
            "Standard Shooting statistics.\n\n"
        )
        file.write("https://fbref.com/en/\n")
        

    print("\nResults saved to:")
    print(RESULTS_FILE)

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print("\nFiles generated:")
    print(f"\n1. Processed dataset:\n   {FILTERED_FILE}")
    print(f"\n2. Results:\n   {RESULTS_FILE}")
    print(f"\n3. Histogram:\n   {HISTOGRAM_FILE}")
    print(f"\n4. Boxplot:\n   {BOXPLOT_FILE}")
    print(f"\n5. T-distribution:\n   {T_DISTRIBUTION_FILE}")

    print("\nAll three graphs were displayed during the analysis.")
    print("\nNo directory was opened automatically.")
    
    plt.show()



if __name__ == "__main__":
    main()