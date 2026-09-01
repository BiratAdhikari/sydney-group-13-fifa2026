# ==============================================================================
# HIT137 Assessment 2 - Question 1
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
import math

import pandas as pd
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


# ==============================================================================
# PROJECT ROOT
# ==============================================================================

# Project structure:
#
# sydney-group-13-fifa2026/
#
# ├── data/
# │   ├── raw/
# │   │   └── raw1.csv
# │   └── processed/
# │       └── processed1.csv
# │
# ├── docs/
# │   └── task1.md
# │
# ├── figures/
# │   └── task1/
# │       ├── histogram.png
# │       ├── boxplot.png
# │       └── t_distribution.png
# │
# ├── notebooks/
# │   └── task1.ipynb
# │
# ├── scripts/
# │   └── task1.py
# │
# └── src/
#     └── Utility.py
#
# task1.py is inside scripts/, so the project root is one directory above.


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# ==============================================================================
# IMPORT UTILITY FUNCTION
# ==============================================================================

if PROJECT_ROOT not in sys.path:
    sys.path.insert(
        0,
        PROJECT_ROOT
    )


from src.Utility import ci_mean


# ==============================================================================
# FILE PATHS
# ==============================================================================

RAW_FILE = os.path.join(
    PROJECT_ROOT,
    "data",
    "raw",
    "raw1.csv"
)


FILTERED_FILE = os.path.join(
    PROJECT_ROOT,
    "data",
    "processed",
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


# ==============================================================================
# SETTINGS
# ==============================================================================

RANDOM_SEED = 137

TOTAL_SAMPLE_SIZE = 35

UNDER25_SAMPLE_SIZE = 10

AGE28PLUS_SAMPLE_SIZE = 25

ALPHA = 0.05


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

def main():

    # ==========================================================================
    # CREATE REQUIRED DIRECTORIES
    # ==========================================================================

    os.makedirs(
        os.path.join(
            PROJECT_ROOT,
            "data",
            "processed"
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
    # 1. DATA WRANGLING
    # ==========================================================================

    print("=" * 60)
    print("1. DATA WRANGLING")
    print("=" * 60)


    # --------------------------------------------------------------------------
    # Check raw dataset.
    # --------------------------------------------------------------------------

    if not os.path.exists(RAW_FILE):

        raise FileNotFoundError(
            "\nRaw dataset was not found.\n\n"
            f"Expected location:\n{RAW_FILE}\n\n"
            "Please make sure raw1.csv is inside data/raw/."
        )


    # --------------------------------------------------------------------------
    # Read raw CSV as text.
    # --------------------------------------------------------------------------

    with open(
        RAW_FILE,
        "r",
        encoding="utf-8-sig"
    ) as file:

        lines = file.readlines()


    # --------------------------------------------------------------------------
    # Find actual FBref header.
    # --------------------------------------------------------------------------

    header_line_number = None


    for i, line in enumerate(lines):

        clean_line = line.strip()


        if (
            clean_line.startswith("Rk,")
            and "Player" in clean_line
            and "Pos" in clean_line
            and "Age" in clean_line
            and "Sh/90" in clean_line
        ):

            header_line_number = i

            break


    # --------------------------------------------------------------------------
    # Stop if header cannot be found.
    # --------------------------------------------------------------------------

    if header_line_number is None:

        print(
            "\nERROR: The real FBref table header could not be found."
        )

        print(
            "\nThe first 10 lines of the file are:"
        )

        for line in lines[:10]:

            print(
                line.strip()
            )

        raise ValueError(
            "Could not find the FBref table header."
        )


    print(
        f"\nActual FBref header found at CSV line: "
        f"{header_line_number + 1}"
    )


    # --------------------------------------------------------------------------
    # Read CSV from actual header.
    # --------------------------------------------------------------------------

    df = pd.read_csv(
        RAW_FILE,
        skiprows=header_line_number
    )


    # --------------------------------------------------------------------------
    # Clean column names.
    # --------------------------------------------------------------------------

    df.columns = (
        df.columns
        .astype(str)
        .str.replace(
            r"[\r\n]",
            "",
            regex=True
        )
        .str.strip()
    )


    print(
        "\nColumns found:"
    )

    print(
        df.columns.tolist()
    )


    original_records = len(df)


    print(
        f"\nOriginal number of records: "
        f"{original_records}"
    )


    # ==========================================================================
    # CHECK REQUIRED COLUMNS
    # ==========================================================================

    required_columns = [
        "Player",
        "Pos",
        "Squad",
        "Age",
        "Sh/90"
    ]


    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]


    if missing_columns:

        print(
            "\nERROR: Required columns are missing:"
        )

        print(
            missing_columns
        )

        print(
            "\nAvailable columns:"
        )

        print(
            df.columns.tolist()
        )

        raise ValueError(
            "The required FBref columns are missing."
        )


    # ==========================================================================
    # CLEAN DATA VALUES
    # ==========================================================================

    df["Player"] = (
        df["Player"]
        .astype(str)
        .str.strip()
    )


    df["Pos"] = (
        df["Pos"]
        .astype(str)
        .str.strip()
    )


    # Remove FBref country-code prefix.
    #
    # Example:
    # es Spain -> Spain

    df["Squad"] = (
        df["Squad"]
        .astype(str)
        .str.strip()
        .str.split(
            " ",
            n=1
        )
        .str[-1]
    )


    # Convert Age.

    df["Age"] = pd.to_numeric(
        df["Age"],
        errors="coerce"
    )


    # Convert Shots/90.

    df["Sh/90"] = pd.to_numeric(
        df["Sh/90"],
        errors="coerce"
    )


    # ==========================================================================
    # REMOVE INVALID RECORDS
    # ==========================================================================

    before_cleaning = len(df)


    df = df.dropna(
        subset=[
            "Player",
            "Pos",
            "Age",
            "Sh/90"
        ]
    ).copy()


    after_cleaning = len(df)


    records_removed = (
        before_cleaning
        - after_cleaning
    )


    print(
        f"\nRecords removed during cleaning: "
        f"{records_removed}"
    )


    # ==========================================================================
    # FILTER ATTACKING PLAYERS
    # ==========================================================================

    # Operational definition:
    #
    # A player is considered an attacking player when their FBref
    # position contains "FW".
    #
    # Included:
    # FW
    # FWMF
    # MFFW
    #
    # Excluded:
    # DF
    # MF
    # GK

    attackers = df[
        df["Pos"].str.contains(
            "FW",
            case=False,
            na=False
        )
    ].copy()


    print(
        f"\nAttacking players found: "
        f"{len(attackers)}"
    )


    # ==========================================================================
    # CREATE AGE GROUPS
    # ==========================================================================

    under25_all = attackers[
        attackers["Age"] < 25
    ].copy()


    age28plus_all = attackers[
        attackers["Age"] >= 28
    ].copy()


    print(
        f"\nUnder 25 attacking players available: "
        f"{len(under25_all)}"
    )


    print(
        f"Age 28+ attacking players available: "
        f"{len(age28plus_all)}"
    )


    # ==========================================================================
    # 2. DATA PREPARATION AND SAMPLING
    # ==========================================================================

    print("\n" + "=" * 60)
    print("2. DATA PREPARATION AND SAMPLING")
    print("=" * 60)


    print(
        "\nPopulation:"
    )

    print(
        "All attacking players in the supplied "
        "FIFA World Cup 2026 player dataset."
    )


    print(
        "\nSampling method:"
    )

    print(
        "Random sampling with a fixed random seed."
    )


    print(
        f"\nRandom seed: {RANDOM_SEED}"
    )


    # ==========================================================================
    # CHECK SAMPLE AVAILABILITY
    # ==========================================================================

    if len(under25_all) < UNDER25_SAMPLE_SIZE:

        raise ValueError(
            "There are not enough Under 25 attacking players."
        )


    if len(age28plus_all) < AGE28PLUS_SAMPLE_SIZE:

        raise ValueError(
            "There are not enough Age 28+ attacking players."
        )


    # ==========================================================================
    # SELECT REPRODUCIBLE SAMPLE
    # ==========================================================================

    under25_sample = under25_all.sample(
        n=UNDER25_SAMPLE_SIZE,
        random_state=RANDOM_SEED
    )


    age28plus_sample = age28plus_all.sample(
        n=AGE28PLUS_SAMPLE_SIZE,
        random_state=RANDOM_SEED
    )


    # ==========================================================================
    # COMBINE GROUPS
    # ==========================================================================

    filtered_df = pd.concat(
        [
            under25_sample,
            age28plus_sample
        ],
        ignore_index=True
    )


    # Shuffle the final sample.

    filtered_df = filtered_df.sample(
        frac=1,
        random_state=RANDOM_SEED
    ).reset_index(
        drop=True
    )


    # ==========================================================================
    # VERIFY SAMPLE
    # ==========================================================================

    if len(filtered_df) != TOTAL_SAMPLE_SIZE:

        raise ValueError(
            "The filtered dataset does not contain exactly 35 records."
        )


    # ==========================================================================
    # SAVE PROCESSED DATA
    # ==========================================================================

    filtered_df.to_csv(
        FILTERED_FILE,
        index=False
    )


    print(
        f"\nRecords used for analysis: "
        f"{len(filtered_df)}"
    )


    print(
        f"Records excluded from original dataset: "
        f"{original_records - len(filtered_df)}"
    )


    print(
        "\nProcessed dataset saved to:"
    )

    print(
        FILTERED_FILE
    )


    # ==========================================================================
    # RELOAD PROCESSED DATA
    # ==========================================================================

    df = pd.read_csv(
        FILTERED_FILE
    )


    df["Age"] = pd.to_numeric(
        df["Age"],
        errors="coerce"
    )


    df["Sh/90"] = pd.to_numeric(
        df["Sh/90"],
        errors="coerce"
    )


    # ==========================================================================
    # FINAL GROUPS
    # ==========================================================================

    under25 = df[
        df["Age"] < 25
    ].copy()


    age28plus = df[
        df["Age"] >= 28
    ].copy()


    print(
        "\nFinal group sizes:"
    )


    print(
        f"Under 25: {len(under25)}"
    )


    print(
        f"Age 28+: {len(age28plus)}"
    )


    # ==========================================================================
    # 3. DESCRIPTIVE STATISTICS
    # ==========================================================================

    print("\n" + "=" * 60)
    print("3. DESCRIPTIVE STATISTICS")
    print("=" * 60)


    def describe_group(sample, label):

        arr = np.array(
            sample,
            dtype=float
        )


        n = len(arr)

        mean_v = arr.mean()

        median_v = np.median(arr)

        min_v = arr.min()

        max_v = arr.max()

        range_v = max_v - min_v

        variance_v = arr.var(
            ddof=1
        )

        std_v = arr.std(
            ddof=1
        )

        q1, q3 = np.percentile(
            arr,
            [25, 75]
        )

        iqr_v = q3 - q1


        print(
            f"\n{label}"
        )

        print(
            "-" * 40
        )

        print(
            f"Sample size (n): {n}"
        )

        print(
            f"Mean: {mean_v:.3f}"
        )

        print(
            f"Median: {median_v:.3f}"
        )

        print(
            f"Minimum: {min_v:.3f}"
        )

        print(
            f"Maximum: {max_v:.3f}"
        )

        print(
            f"Range: {range_v:.3f}"
        )

        print(
            f"Variance: {variance_v:.3f}"
        )

        print(
            f"Standard deviation: {std_v:.3f}"
        )

        print(
            f"Q1: {q1:.3f}"
        )

        print(
            f"Q3: {q3:.3f}"
        )

        print(
            f"IQR: {iqr_v:.3f}"
        )


        return {
            "n": n,
            "mean": mean_v,
            "median": median_v,
            "min": min_v,
            "max": max_v,
            "range": range_v,
            "variance": variance_v,
            "std_dev": std_v,
            "q1": q1,
            "q3": q3,
            "iqr": iqr_v
        }


    stats_u25 = describe_group(
        under25["Sh/90"],
        "Under 25"
    )


    stats_28plus = describe_group(
        age28plus["Sh/90"],
        "Age 28+"
    )


    # ==========================================================================
    # 4. HISTOGRAM
    # ==========================================================================

    print("\n" + "=" * 60)
    print("4. VISUALISATIONS")
    print("=" * 60)


    print(
        "\nCreating histogram..."
    )


    plt.figure(
        figsize=(10, 6)
    )


    plt.hist(
        under25["Sh/90"],
        bins=8,
        alpha=0.6,
        edgecolor="black",
        label="Under 25"
    )


    plt.hist(
        age28plus["Sh/90"],
        bins=8,
        alpha=0.6,
        edgecolor="black",
        label="Age 28+"
    )


    plt.title(
        "Histogram of Shots/90 - Under 25 vs Age 28+"
    )


    plt.xlabel(
        "Shots per 90 minutes"
    )


    plt.ylabel(
        "Number of players"
    )


    plt.legend()


    plt.tight_layout()


    plt.savefig(
        HISTOGRAM_FILE,
        dpi=300,
        bbox_inches="tight"
    )


    print(
        f"Histogram saved to:\n{HISTOGRAM_FILE}"
    )


    # ==========================================================================
    # DISPLAY HISTOGRAM
    # ==========================================================================

    plt.show()


    # ==========================================================================
    # 5. BOXPLOT
    # ==========================================================================

    print(
        "\nCreating boxplot..."
    )


    plt.figure(
        figsize=(8, 6)
    )


    plt.boxplot(
        [
            under25["Sh/90"],
            age28plus["Sh/90"]
        ],
        tick_labels=[
            "Under 25",
            "Age 28+"
        ]
    )


    plt.title(
        "Boxplot of Shots/90 - Under 25 vs Age 28+"
    )


    plt.ylabel(
        "Shots per 90 minutes"
    )


    plt.tight_layout()


    plt.savefig(
        BOXPLOT_FILE,
        dpi=300,
        bbox_inches="tight"
    )


    print(
        f"Boxplot saved to:\n{BOXPLOT_FILE}"
    )


    # ==========================================================================
    # DISPLAY BOXPLOT
    # ==========================================================================

    plt.show()


    # ==========================================================================
    # 6. CONFIDENCE INTERVAL
    # ==========================================================================

    print("\n" + "=" * 60)
    print("5. INFERENTIAL STATISTICS - CONFIDENCE INTERVAL")
    print("=" * 60)


    # --------------------------------------------------------------------------
    # Under 25
    # --------------------------------------------------------------------------

    (
        x_bar1,
        s1,
        n1,
        ci_low1,
        ci_upp1
    ) = ci_mean(
        under25["Sh/90"]
    )


    print(
        "\nUnder 25:"
    )


    print(
        f"Mean: {x_bar1:.3f}"
    )


    print(
        f"Standard deviation: {s1:.3f}"
    )


    print(
        f"Sample size: {n1}"
    )


    print(
        f"95% Confidence Interval: "
        f"{ci_low1:.3f} to {ci_upp1:.3f}"
    )


    # --------------------------------------------------------------------------
    # Age 28+
    # --------------------------------------------------------------------------

    (
        x_bar2,
        s2,
        n2,
        ci_low2,
        ci_upp2
    ) = ci_mean(
        age28plus["Sh/90"]
    )


    print(
        "\nAge 28+:"
    )


    print(
        f"Mean: {x_bar2:.3f}"
    )


    print(
        f"Standard deviation: {s2:.3f}"
    )


    print(
        f"Sample size: {n2}"
    )


    print(
        f"95% Confidence Interval: "
        f"{ci_low2:.3f} to {ci_upp2:.3f}"
    )


    # ==========================================================================
    # 7. WELCH TWO-SAMPLE T-TEST
    # ==========================================================================

    print("\n" + "=" * 60)
    print("6. INFERENTIAL STATISTICS - TWO-SAMPLE T-TEST")
    print("=" * 60)


    print(
        "\nNull hypothesis (H0):"
    )


    print(
        "There is no difference in mean Shots/90 "
        "between attacking players under 25 and "
        "attacking players aged 28+."
    )


    print(
        "\nAlternative hypothesis (H1):"
    )


    print(
        "There is a difference in mean Shots/90 "
        "between attacking players under 25 and "
        "attacking players aged 28+."
    )


    print(
        f"\nSignificance level: {ALPHA}"
    )


    # --------------------------------------------------------------------------
    # Welch t-test
    # --------------------------------------------------------------------------

    t_statistic, p_value = st.ttest_ind(
        under25["Sh/90"],
        age28plus["Sh/90"],
        equal_var=False,
        alternative="two-sided"
    )


    # --------------------------------------------------------------------------
    # Welch-Satterthwaite degrees of freedom
    # --------------------------------------------------------------------------

    welch_df = (
        (
            s1**2 / n1
            +
            s2**2 / n2
        ) ** 2
    ) / (
        (
            (s1**2 / n1) ** 2
            /
            (n1 - 1)
        )
        +
        (
            (s2**2 / n2) ** 2
            /
            (n2 - 1)
        )
    )


    print(
        f"\nt-statistic: "
        f"{t_statistic:.3f}"
    )


    print(
        f"Degrees of freedom: "
        f"{welch_df:.3f}"
    )


    print(
        f"p-value: "
        f"{p_value:.4f}"
    )


    # ==========================================================================
    # DECISION
    # ==========================================================================

    if p_value < ALPHA:

        decision = "Reject H0"

        conclusion = (
            "There is statistically significant evidence "
            "of a difference in mean Shots/90 between "
            "attacking players under 25 and attacking "
            "players aged 28+."
        )

    else:

        decision = "Fail to reject H0"

        conclusion = (
            "There is not enough statistical evidence "
            "to conclude that the mean Shots/90 differs "
            "between attacking players under 25 and "
            "attacking players aged 28+."
        )


    print(
        f"\nDecision: {decision}"
    )


    print(
        f"\nConclusion:\n{conclusion}"
    )


    # ==========================================================================
    # 8. T-DISTRIBUTION GRAPH
    # ==========================================================================

    print("\n" + "=" * 60)
    print("7. T-DISTRIBUTION VISUALISATION")
    print("=" * 60)


    critical_t = st.t.ppf(
        1 - ALPHA / 2,
        welch_df
    )


    # Create t-distribution range.

    x = np.linspace(
        -5,
        5,
        500
    )


    y = st.t.pdf(
        x,
        welch_df
    )


    print(
        "\nCreating t-distribution graph..."
    )


    plt.figure(
        figsize=(10, 6)
    )


    # t-distribution curve.

    plt.plot(
        x,
        y,
        linewidth=2,
        label=(
            f"t-distribution "
            f"(df={welch_df:.2f})"
        )
    )


    # Positive critical value.

    plt.axvline(
        critical_t,
        linestyle="--",
        label=(
            f"Critical t = "
            f"{critical_t:.2f}"
        )
    )


    # Negative critical value.

    plt.axvline(
        -critical_t,
        linestyle="--"
    )


    # Observed t-statistic.

    plt.axvline(
        t_statistic,
        linewidth=2,
        label=(
            f"Observed t = "
            f"{t_statistic:.2f}"
        )
    )


    # Rejection regions.

    plt.fill_between(
        x,
        y,
        where=(
            (x >= critical_t)
            |
            (x <= -critical_t)
        ),
        alpha=0.2
    )


    plt.title(
        "t-distribution: Shots/90 "
        "Under 25 vs Age 28+"
    )


    plt.xlabel(
        "t"
    )


    plt.ylabel(
        "Probability density"
    )


    plt.legend()


    plt.tight_layout()


    plt.savefig(
        T_DISTRIBUTION_FILE,
        dpi=300,
        bbox_inches="tight"
    )


    print(
        f"T-distribution graph saved to:\n"
        f"{T_DISTRIBUTION_FILE}"
    )


    # ==========================================================================
    # DISPLAY T-DISTRIBUTION
    # ==========================================================================

    plt.show()


    # ==========================================================================
    # 9. SAVE RESULTS TO MARKDOWN
    # ==========================================================================

    print("\n" + "=" * 60)
    print("8. SAVING RESULTS")
    print("=" * 60)


    mean_difference = (
        stats_u25["mean"]
        -
        stats_28plus["mean"]
    )


    # --------------------------------------------------------------------------
    # Relative paths for Markdown.
    # --------------------------------------------------------------------------

    histogram_md = (
        "../figures/task1/histogram.png"
    )


    boxplot_md = (
        "../figures/task1/boxplot.png"
    )


    t_distribution_md = (
        "../figures/task1/t_distribution.png"
    )


    # --------------------------------------------------------------------------
    # Write Markdown results.
    # --------------------------------------------------------------------------

    with open(
        RESULTS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "# Question 1 Results\n\n"
        )


        file.write(
            "## Analytical Question\n\n"
        )


        file.write(
            "> Is there a statistically significant difference "
            "in Shots/90 between attacking players under 25 "
            "and attacking players aged 28+?\n\n"
        )


        # ======================================================================
        # DATASET
        # ======================================================================

        file.write(
            "## Dataset\n\n"
        )


        file.write(
            "The analysis uses FIFA World Cup 2026 player "
            "shooting statistics obtained from FBref.\n\n"
        )


        file.write(
            "- Raw dataset: `data/raw/raw1.csv`\n"
        )


        file.write(
            f"- Original records: **{original_records}**\n"
        )


        file.write(
            f"- Records removed during cleaning: "
            f"**{records_removed}**\n"
        )


        file.write(
            f"- Attacking players identified: "
            f"**{len(attackers)}**\n\n"
        )


        # ======================================================================
        # DATA WRANGLING
        # ======================================================================

        file.write(
            "## 1. Data Wrangling\n\n"
        )


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
            f"- Original records: **{original_records}**\n"
        )


        file.write(
            f"- Records removed during cleaning: "
            f"**{records_removed}**\n"
        )


        file.write(
            f"- Attacking players: **{len(attackers)}**\n"
        )


        file.write(
            f"- Under 25 available: **{len(under25_all)}**\n"
        )


        file.write(
            f"- Age 28+ available: **{len(age28plus_all)}**\n\n"
        )


        # ======================================================================
        # DATA PREPARATION
        # ======================================================================

        file.write(
            "## 2. Data Preparation and Sampling\n\n"
        )


        file.write(
            "- Under 25 group: `Age < 25`\n"
        )


        file.write(
            "- Age 28+ group: `Age >= 28`\n"
        )


        file.write(
            "- Players aged 25, 26 and 27 were excluded.\n"
        )


        file.write(
            "- Sampling method: Random sampling.\n"
        )


        file.write(
            f"- Fixed random seed: **{RANDOM_SEED}**\n"
        )


        file.write(
            f"- Final sample size: **{len(df)}**\n"
        )


        file.write(
            f"- Under 25 sample: **{len(under25)}**\n"
        )


        file.write(
            f"- Age 28+ sample: **{len(age28plus)}**\n\n"
        )


        file.write(
            "The processed dataset is saved as "
            "`data/processed/processed1.csv`.\n\n"
        )


        # ======================================================================
        # DESCRIPTIVE STATISTICS
        # ======================================================================

        file.write(
            "## 3. Descriptive Statistics\n\n"
        )


        file.write(
            "| Statistic | Under 25 | Age 28+ |\n"
        )


        file.write(
            "|---|---:|---:|\n"
        )


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


        # ======================================================================
        # CONFIDENCE INTERVAL
        # ======================================================================

        file.write(
            "## 4. 95% Confidence Interval\n\n"
        )


        file.write(
            "| Age Group | Mean | Standard Deviation | "
            "n | 95% Confidence Interval |\n"
        )


        file.write(
            "|---|---:|---:|---:|---|\n"
        )


        file.write(
            f"| Under 25 | {x_bar1:.3f} | {s1:.3f} | "
            f"{n1} | {ci_low1:.3f} to {ci_upp1:.3f} |\n"
        )


        file.write(
            f"| Age 28+ | {x_bar2:.3f} | {s2:.3f} | "
            f"{n2} | {ci_low2:.3f} to {ci_upp2:.3f} |\n\n"
        )


        # ======================================================================
        # T-TEST
        # ======================================================================

        file.write(
            "## 5. Welch Two-Sample t-Test\n\n"
        )


        file.write(
            "### Null Hypothesis (H0)\n\n"
        )


        file.write(
            "There is no difference in mean Shots/90 between "
            "attacking players under 25 and attacking players "
            "aged 28+.\n\n"
        )


        file.write(
            "### Alternative Hypothesis (H1)\n\n"
        )


        file.write(
            "There is a difference in mean Shots/90 between "
            "attacking players under 25 and attacking players "
            "aged 28+.\n\n"
        )


        file.write(
            f"- Significance level: **α = {ALPHA}**\n"
        )


        file.write(
            f"- t-statistic: **{t_statistic:.3f}**\n"
        )


        file.write(
            f"- Degrees of freedom: **{welch_df:.3f}**\n"
        )


        file.write(
            f"- p-value: **{p_value:.4f}**\n"
        )


        file.write(
            f"- Decision: **{decision}**\n\n"
        )


        # ======================================================================
        # CONCLUSION
        # ======================================================================

        file.write(
            "## 6. Conclusion\n\n"
        )


        file.write(
            f"{conclusion}\n\n"
        )


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


        # ======================================================================
        # VISUALISATIONS
        # ======================================================================

        file.write(
            "## 7. Visualisations\n\n"
        )


        file.write(
            "### Histogram\n\n"
        )


        file.write(
            f"![Shots/90 Histogram]"
            f"({histogram_md})\n\n"
        )


        file.write(
            "### Boxplot\n\n"
        )


        file.write(
            f"![Shots/90 Boxplot]"
            f"({boxplot_md})\n\n"
        )


        file.write(
            "### t-Distribution\n\n"
        )


        file.write(
            f"![Shots/90 t-Distribution]"
            f"({t_distribution_md})\n\n"
        )


        # ======================================================================
        # OUTPUT FILES
        # ======================================================================

        file.write(
            "## 8. Output Files\n\n"
        )


        file.write(
            "- Raw dataset: `data/raw/raw1.csv`\n"
        )


        file.write(
            "- Processed dataset: `data/processed/processed1.csv`\n"
        )


        file.write(
            "- Analysis script: `scripts/task1.py`\n"
        )


        file.write(
            "- Confidence interval function: `src/Utility.py`\n"
        )


        file.write(
            "- Histogram: `figures/task1/histogram.png`\n"
        )


        file.write(
            "- Boxplot: `figures/task1/boxplot.png`\n"
        )


        file.write(
            "- t-Distribution: `figures/task1/t_distribution.png`\n\n"
        )


        # ======================================================================
        # DATA SOURCE
        # ======================================================================

        file.write(
            "## 9. Data Source\n\n"
        )


        file.write(
            "FBref.com (Sports Reference), FIFA World Cup "
            "Standard Shooting statistics.\n\n"
        )


        file.write(
            "https://fbref.com/en/\n"
        )


    print(
        "\nResults saved to:"
    )


    print(
        RESULTS_FILE
    )


    # ==========================================================================
    # FINAL SUMMARY
    # ==========================================================================

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 60)


    print(
        "\nFiles generated:"
    )


    print(
        f"\n1. Processed dataset:"
        f"\n   {FILTERED_FILE}"
    )


    print(
        f"\n2. Results:"
        f"\n   {RESULTS_FILE}"
    )


    print(
        f"\n3. Histogram:"
        f"\n   {HISTOGRAM_FILE}"
    )


    print(
        f"\n4. Boxplot:"
        f"\n   {BOXPLOT_FILE}"
    )


    print(
        f"\n5. T-distribution:"
        f"\n   {T_DISTRIBUTION_FILE}"
    )


    print(
        "\nAll three graphs were displayed during the analysis."
    )


    print(
        "\nNo directory was opened automatically."
    )


# ==============================================================================
# RUN PROGRAM
# ==============================================================================

if __name__ == "__main__":

    main()