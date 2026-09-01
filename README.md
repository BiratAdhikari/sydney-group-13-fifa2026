# Sydney Group 13 - FIFA World Cup 2026 Analytics

## HIT137 Foundations of Data Science - Final Assessment

This repository contains the code, datasets, documentation, visualisations, and Jupyter Notebook for **Objective 1** of the FIFA World Cup 2026 data analytics project.

The project investigates four analytical questions using football statistics sourced from **FBref**, **FIFA**, and **The Stats Don't Lie**.

---

# Team Members

| Student Name         | Student ID  |
| -------------------- | ----------- |
| Birat Adhikari       | To be added |
| **Hemanta Adhikari** | **s403355** |
| John Karki           | To be added |
| Muhammad Hussnain    | To be added |

> **Question 1 was completed by Hemanta Adhikari (Student ID: s403355).**

---

# Analytical Questions

The team is investigating four different analytical questions.

## Question 1 - Shots/90 and Age

> **Is there a statistically significant difference in Shots/90 between attacking players under 25 and attacking players aged 28+?**

**Completed by:** Hemanta Adhikari
**Student ID:** s403355

### Main variables

* Player
* Player position
* Player age
* Shots/90

### Statistical methods

* Data wrangling
* Data cleaning
* Data preparation and sampling
* Descriptive statistics
* 95% confidence intervals
* Welch two-sample t-test
* t-distribution visualisation

---

## Question 2 - Tackles/90 and Player Position

> **Do defenders win significantly more tackles per 90 minutes than midfielders and forwards?**

**Main variables:**

* Player position
* Tackles/90

---

## Question 3 - Fouls/90 and Starting Percentage

> **Do players who started at least 50% of their team's matches commit significantly more Fouls/90 than players who started fewer than 50%?**

**Main variables:**

* Starting percentage
* Fouls/90

---

## Question 4 - Possession and SoT%

> **Do teams with average possession above 55% have a significantly higher SoT% than teams with possession of 55% or below?**

**Main variables:**

* Team possession
* SoT%

---

# Question 1 - Shots/90 Analysis

## Student Information

**Student Name:** Hemanta Adhikari
**Student ID:** s403355

### Analytical Question

> **Is there a statistically significant difference in Shots/90 between attacking players under 25 and attacking players aged 28+?**

The purpose of Question 1 is to investigate whether attacking players in two different age groups have significantly different shooting frequencies.

The shooting measure used is **Shots/90**, representing the number of shots taken per 90 minutes.

---

# Question 1 Data Source

Question 1 uses player shooting statistics from **FBref's Player Shooting table** for the FIFA World Cup 2026 competition.

**Data source:** FBref - Sports Reference

**Competition:** FIFA World Cup

**Statistics table:** Player Shooting

**Source page:** FBref World Cup Player Shooting Statistics

The raw dataset used in the project is:

```text
data/raw/raw1.csv
```

The source page is:

https://fbref.com/en/comps/1/shooting/World-Cup-Stats

---

# Question 1 Workflow

The complete Question 1 workflow is:

```text
FBref Player Shooting Data
          |
          v
     raw1.csv
          |
          v
   Data Wrangling
          |
          v
     Data Cleaning
          |
          v
 Identify Attacking Players
          |
          v
     Create Age Groups
          |
          +----------------------+
          |                      |
          v                      v
      Under 25                Age 28+
          |                      |
          +----------+-----------+
                     |
                     v
          Random Sampling
          Under 25 = 10
          Age 28+   = 25
                     |
                     v
             Total Sample = 35
                     |
                     v
        processed1.csv
                     |
                     v
       Descriptive Statistics
                     |
                     v
            Visualisations
                     |
          +----------+----------+
          |          |           |
          v          v           v
      Histogram   Boxplot   t-Distribution
                     |
                     v
          95% Confidence Interval
                     |
                     v
        Welch Two-Sample t-Test
                     |
                     v
               Conclusion
                     |
                     v
             task1.md
                     |
                     v
             task1.ipynb
```

---

# Project Structure

The current repository structure is:

```text
sydney-group-13-fifa2026/
│
├── data/
│   ├── processed/
│   │   └── processed1.csv
│   │
│   └── raw/
│       └── raw1.csv
│
├── docs/
│   └── task1.md
│
├── figures/
│   └── task1/
│       ├── histogram.png
│       ├── boxplot.png
│       └── t_distribution.png
│
├── notebooks/
│   └── task1.ipynb
│
├── scripts/
│   └── task1.py
│
├── src/
│   └── Utility.py
│
├── README.md
│
└── requirements.txt
```

---

# Folder and File Descriptions

## `data/raw/`

Contains the original, unmodified dataset collected from FBref.

```text
data/raw/raw1.csv
```

This file is the starting point for the Question 1 analysis.

The script reads the raw CSV and identifies the actual FBref table header before processing the data.

---

## `data/processed/`

Contains the processed dataset generated by `task1.py`.

```text
data/processed/processed1.csv
```

For Question 1, the final reproducible sample contains **35 attacking players**:

| Age Group | Sample Size |
| --------- | ----------: |
| Under 25  |          10 |
| Age 28+   |          25 |
| **Total** |      **35** |

---

## `docs/`

Contains the automatically generated written results.

```text
docs/task1.md
```

The `task1.md` file is generated by:

```text
scripts/task1.py
```

It contains:

* Analytical question
* Data wrangling
* Data cleaning
* Data preparation
* Sampling information
* Descriptive statistics
* Confidence intervals
* Hypotheses
* Welch t-test results
* Statistical conclusion
* Visualisations
* Output files
* Data source

---

# `figures/task1/`

All Question 1 visualisations are saved inside:

```text
figures/task1/
```

The script generates:

```text
figures/task1/
├── histogram.png
├── boxplot.png
└── t_distribution.png
```

### Histogram

The histogram compares the distribution of Shots/90 between:

* Under 25 attacking players
* Age 28+ attacking players

### Boxplot

The boxplot compares:

* Median
* Spread
* Quartiles
* Potential outliers

between the two age groups.

### t-Distribution

The t-distribution graph displays:

* Welch t-distribution
* Positive critical t-value
* Negative critical t-value
* Observed t-statistic
* Rejection regions

The graphs are saved automatically and are also displayed when the script finishes running.

The script does **not** redirect the user to the `figures/task1/` directory.

---

# `notebooks/task1.ipynb`

The Question 1 Jupyter Notebook is stored at:

```text
notebooks/task1.ipynb
```

The notebook is automatically generated/populated by the Question 1 analysis workflow.

This means the user does not need to manually create the notebook content before running the analysis.

The notebook provides a notebook-based record of the Question 1 analysis, including the main processing steps, statistical calculations, results, and visualisations.

After running:

```bash
python scripts/task1.py
```

the notebook is generated or updated automatically.

---

# `scripts/task1.py`

This is the main Python program for Question 1.

It performs the complete analysis workflow:

1. Locate the project root.
2. Locate the raw dataset.
3. Read the FBref CSV.
4. Detect the actual FBref table header.
5. Clean column names.
6. Check required columns.
7. Clean player, position, squad, age and Shots/90 values.
8. Remove invalid records.
9. Identify attacking players.
10. Create the Under 25 group.
11. Create the Age 28+ group.
12. Randomly sample 10 Under 25 players.
13. Randomly sample 25 Age 28+ players.
14. Combine the samples into 35 records.
15. Save the processed dataset.
16. Calculate descriptive statistics.
17. Generate the histogram.
18. Generate the boxplot.
19. Calculate 95% confidence intervals.
20. Perform the Welch two-sample t-test.
21. Generate the t-distribution visualisation.
22. Generate `docs/task1.md`.
23. Generate/update `notebooks/task1.ipynb`.
24. Display the generated graphs.

---

# `src/Utility.py`

The `src/Utility.py` file contains shared statistical utility functions.

For Question 1, the `ci_mean()` function is used to calculate the 95% confidence interval for the mean Shots/90.

The Question 1 script imports the function using:

```python
from src.Utility import ci_mean
```

---

# Question 1 Data Wrangling

The analysis first reads:

```text
data/raw/raw1.csv
```

The script searches for the actual FBref table header rather than assuming that the header is on the first line of the CSV.

The following columns are required:

```text
Player
Pos
Squad
Age
Sh/90
```

### Cleaning steps

1. Clean column names.
2. Remove unnecessary whitespace.
3. Clean player names.
4. Clean player positions.
5. Remove the FBref country-code prefix from Squad.
6. Convert Age to numeric.
7. Convert Sh/90 to numeric.
8. Remove records with missing Player, Pos, Age or Sh/90 values.
9. Retain valid zero Shots/90 observations.

---

# Definition of Attacking Players

For Question 1, an attacking player is operationally defined using the FBref position field.

A player is classified as an attacking player when their position contains:

```text
FW
```

This includes positions such as:

```text
FW
FWMF
MFFW
```

Positions such as:

```text
GK
DF
MF
```

are excluded.

This definition is applied consistently throughout the analysis.

---

# Age Groups

The analysis compares two age groups.

## Under 25

```text
Age < 25
```

## Age 28+

```text
Age >= 28
```

Players aged:

```text
25
26
27
```

are excluded from the comparison because they do not belong to either age group specified in the analytical question.

---

# Sampling

The final analysis uses a sample of **35 attacking players**.

The sample is divided as follows:

| Age Group | Number of Players |
| --------- | ----------------: |
| Under 25  |                10 |
| Age 28+   |                25 |
| **Total** |            **35** |

A fixed random seed is used:

```text
137
```

Using a fixed random seed makes the sampling process reproducible.

The final dataset is saved to:

```text
data/processed/processed1.csv
```

---

# Descriptive Statistics

The following descriptive statistics are calculated for both age groups:

* Sample size
* Mean
* Median
* Minimum
* Maximum
* Range
* Variance
* Standard deviation
* Q1
* Q3
* IQR

The results are automatically written to:

```text
docs/task1.md
```

---

# 95% Confidence Interval

A 95% confidence interval is calculated for the mean Shots/90 of each age group.

The calculation uses:

```text
src/Utility.py
```

The results are included in:

```text
docs/task1.md
```

---

# Welch Two-Sample t-Test

A **Welch two-sample t-test** is used to compare the mean Shots/90 of the two independent age groups.

Welch's test is used because it does not require the two groups to have equal population variances.

The test is two-tailed.

## Null Hypothesis (H0)

> There is no difference in mean Shots/90 between attacking players under 25 and attacking players aged 28+.

## Alternative Hypothesis (H1)

> There is a difference in mean Shots/90 between attacking players under 25 and attacking players aged 28+.

## Significance Level

```text
α = 0.05
```

The test is performed using:

```python
scipy.stats.ttest_ind(
    under25["Sh/90"],
    age28plus["Sh/90"],
    equal_var=False,
    alternative="two-sided"
)
```

---

# Question 1 Result

Based on the current Question 1 analysis:

```text
t-statistic = -0.014
degrees of freedom = 22.698
p-value = 0.9889
```

The significance level is:

```text
α = 0.05
```

Because:

```text
p-value > 0.05
```

the decision is:

> **Fail to reject H0.**

Therefore:

> There is not enough statistical evidence to conclude that the mean Shots/90 differs between attacking players under 25 and attacking players aged 28+.

The very small difference between the sample means does not provide evidence of a statistically significant difference.

Failing to reject the null hypothesis does **not** prove that the population means are exactly equal. It means that the available sample does not provide sufficient statistical evidence to establish a significant difference.

The detailed results are automatically written to:

```text
docs/task1.md
```

---

# Running Question 1

From the project root, run:

```bash
python scripts/task1.py
```

The project root should contain:

```text
data/
docs/
figures/
notebooks/
scripts/
src/
README.md
requirements.txt
```

Before running the analysis, install the required Python packages:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python scripts/task1.py
```

---

# Automatic Outputs

When `task1.py` completes successfully, it automatically creates or updates the Question 1 outputs.

## Processed dataset

```text
data/processed/processed1.csv
```

## Results report

```text
docs/task1.md
```

## Histogram

```text
figures/task1/histogram.png
```

## Boxplot

```text
figures/task1/boxplot.png
```

## t-Distribution

```text
figures/task1/t_distribution.png
```

## Jupyter Notebook

```text
notebooks/task1.ipynb
```

The generated graphs are also displayed after the analysis finishes.

---

# Jupyter Notebook

The Question 1 notebook is:

```text
notebooks/task1.ipynb
```

It can also be opened manually with Jupyter:

```bash
jupyter notebook notebooks/task1.ipynb
```

or:

```bash
jupyter lab notebooks/task1.ipynb
```

However, the normal Question 1 workflow is to run:

```bash
python scripts/task1.py
```

and allow the analysis script to generate/update the notebook automatically.

---

# Requirements

The main Python libraries used by Question 1 are:

```text
pandas
numpy
scipy
matplotlib
```

The complete dependency list is stored in:

```text
requirements.txt
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

# Output Summary

| Output            | Location                           |
| ----------------- | ---------------------------------- |
| Raw dataset       | `data/raw/raw1.csv`                |
| Processed dataset | `data/processed/processed1.csv`    |
| Question 1 report | `docs/task1.md`                    |
| Histogram         | `figures/task1/histogram.png`      |
| Boxplot           | `figures/task1/boxplot.png`        |
| t-distribution    | `figures/task1/t_distribution.png` |
| Question 1 script | `scripts/task1.py`                 |
| Utility functions | `src/Utility.py`                   |
| Jupyter Notebook  | `notebooks/task1.ipynb`            |

---

# Team Question Summary

| Question | Analytical Focus                 | Comparison                            |
| -------- | -------------------------------- | ------------------------------------- |
| **Q1**   | Shots/90 and age                 | Under 25 vs Age 28+ attacking players |
| **Q2**   | Tackles/90 and position          | Defenders vs midfielders/forwards     |
| **Q3**   | Fouls/90 and starting percentage | Started ≥50% vs <50%                  |
| **Q4**   | SoT% and possession              | Possession >55% vs ≤55%               |

---

# Question 1 Ownership

**Question:** Q1 - Shots/90 and Age

**Completed by:** Hemanta Adhikari

**Student ID:** s403355

**Main analysis script:**

```text
scripts/task1.py
```

**Statistical utility:**

```text
src/Utility.py
```

**Raw dataset:**

```text
data/raw/raw1.csv
```

**Processed dataset:**

```text
data/processed/processed1.csv
```

**Results/documentation:**

```text
docs/task1.md
```

**Jupyter Notebook:**

```text
notebooks/task1.ipynb
```

**Visualisations:**

```text
figures/task1/
```

---

# Repository Information

**Repository:** `sydney-group-13-fifa2026`

**Project:** FIFA World Cup 2026 Analytics - Objective 1

**Question 1:** Shots/90 and Age

**Question 1 Student:** Hemanta Adhikari

**Student ID:** s403355

**Question 1 Data Source:** FBref - Player Shooting Statistics

**Question 1 Source Page:** FBref World Cup Player Shooting Statistics
