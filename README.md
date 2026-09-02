# Sydney Group 13 - FIFA World Cup 2026 Analytics

## HIT137 Foundations of Data Science - Final Assessment

This repository contains the code, datasets, documentation, visualisations, and Jupyter Notebook for the **FIFA World Cup 2026 data analytics project**.

The project investigates four analytical questions using football statistics sourced from **FBref, FIFA, and The Stats Don't Lie**.

Currently, **Question 1 has been completed and implemented as a modular Python analysis workflow**.

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

The team is investigating four analytical questions.

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

### Main variables

* Player position
* Tackles/90

**Status:** To be completed.

---

## Question 3 - Fouls/90 and Starting Percentage

> **Do players who started at least 50% of their team's matches commit significantly more Fouls/90 than players who started fewer than 50%?**

### Main variables

* Starting percentage
* Fouls/90

**Status:** To be completed.

---

## Question 4 - Possession and SoT%

> **Do teams with average possession above 55% have a significantly higher SoT% than teams with possession of 55% or below?**

### Main variables

* Team possession
* SoT%

**Status:** To be completed.

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

Question 1 uses player shooting statistics from the **FBref Player Shooting table** for the FIFA World Cup dataset.

**Data source:** FBref - Sports Reference

**Competition:** FIFA World Cup

**Statistics table:** Player Shooting

**Raw dataset:**

```text
data/raw/raw1.csv
```

**Source page:**

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
│       ├── boxplot.png
│       ├── histogram.png
│       └── t_distribution.png
│
├── notebooks/
│   └── task1.ipynb
│
├── scripts/
│   ├── task1.py
│   └── task2.py
│
├── src/
│   ├── __pycache__/
│   │   └── Utility.cpython-313.pyc
│   │
│   ├── task1/
│   │   ├── confidence_interval.py
│   │   ├── data_preparation.py
│   │   ├── data_wrangling.py
│   │   ├── descriptive_statistics.py
│   │   ├── two_sample_t_test.py
│   │   └── __pycache__/
│   │
│   └── Utility.py
│
├── README.md
└── requirements.txt
```

> `__pycache__` contains Python-generated bytecode files. These files are not part of the analysis and should normally be excluded from Git using `.gitignore`.

---

# Folder and File Descriptions

## `data/`

The `data` directory contains the raw and processed datasets used in the project.

### `data/raw/`

Contains the original dataset used for Question 1.

```text
data/raw/raw1.csv
```

The raw dataset is not modified directly by the analysis.

---

### `data/processed/`

Contains the processed dataset generated by the Question 1 analysis.

```text
data/processed/processed1.csv
```

The final sample contains **35 attacking players**.

| Age Group | Sample Size |
| --------- | ----------: |
| Under 25  |          10 |
| Age 28+   |          25 |
| **Total** |      **35** |

---

# `docs/`

The `docs` directory contains the written results of the analysis.

```text
docs/
└── task1.md
```

The `task1.md` file contains:

* Analytical question
* Data wrangling
* Data preparation
* Sampling
* Descriptive statistics
* Confidence intervals
* Hypotheses
* Welch two-sample t-test
* Statistical conclusion
* Visualisation information
* Data source
* Output information

The report is generated by:

```text
scripts/task1.py
```

---

# `figures/`

The `figures` directory stores visualisations produced by the analysis.

```text
figures/
└── task1/
    ├── boxplot.png
    ├── histogram.png
    └── t_distribution.png
```

## Histogram

The histogram shows the distribution of Shots/90 for:

* Under 25 attacking players
* Age 28+ attacking players

## Boxplot

The boxplot provides a comparison of:

* Median
* Quartiles
* Spread
* Potential outliers

between the two age groups.

## t-Distribution

The t-distribution graph visualises the Welch t-test, including the observed t-statistic and critical regions.

All three figures are saved automatically when the analysis is run.

The figures are displayed together after the complete analysis finishes.

---

# `notebooks/`

The `notebooks` directory contains the Jupyter Notebook for Question 1.

```text
notebooks/
└── task1.ipynb
```

The notebook provides a notebook-based record of the Question 1 analysis.

---

# `scripts/`

The `scripts` directory contains the main executable analysis scripts.

```text
scripts/
├── task1.py
└── task2.py
```

## `scripts/task1.py`

This is the main script for Question 1.

It connects all five analytical stages:

```python
from src.task1.data_wrangling import data_wrangling
from src.task1.data_preparation import data_preparation
from src.task1.descriptive_statistics import descriptive_statistics
from src.task1.confidence_interval import confidence_interval
from src.task1.two_sample_t_test import t_test
```

The script runs the complete Question 1 workflow.

### Main responsibilities

1. Locate the project directory.
2. Load the raw dataset.
3. Perform data wrangling.
4. Prepare the data.
5. Perform random sampling.
6. Save the processed dataset.
7. Calculate descriptive statistics.
8. Generate the histogram.
9. Generate the boxplot.
10. Calculate confidence intervals.
11. Perform the Welch two-sample t-test.
12. Generate the t-distribution graph.
13. Generate the Question 1 report.
14. Display all generated graphs.

---

## `scripts/task2.py`

This file is reserved for the analysis of **Question 2**.

**Status:** To be completed.

---

# `src/`

The `src` directory contains reusable Python modules used by the analysis scripts.

```text
src/
├── task1/
│   ├── confidence_interval.py
│   ├── data_preparation.py
│   ├── data_wrangling.py
│   ├── descriptive_statistics.py
│   └── two_sample_t_test.py
│
└── Utility.py
```

---

# `src/task1/`

The Question 1 analysis has been divided into separate modules so that each analytical component has its own file.

This makes the project easier to read, maintain and test.

---

## `data_wrangling.py`

Responsible for the first stage of the analysis.

It handles:

* Reading the raw CSV
* Finding the actual FBref table header
* Cleaning column names
* Cleaning player information
* Cleaning squad information
* Converting Age to numeric
* Converting Shots/90 to numeric
* Removing invalid records
* Identifying attacking players
* Creating the required age groups

---

## `data_preparation.py`

Responsible for preparing the final sample.

It handles:

* Random sampling
* Fixed random seed
* Selecting 10 Under 25 players
* Selecting 25 Age 28+ players
* Combining the groups
* Shuffling the final sample
* Saving `processed1.csv`

The random seed used is:

```text
137
```

This makes the sampling process reproducible.

---

## `descriptive_statistics.py`

Responsible for calculating descriptive statistics.

The following statistics are calculated:

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

It also creates:

```text
histogram.png
boxplot.png
```

---

## `confidence_interval.py`

Responsible for calculating the 95% confidence interval for the mean Shots/90 of each age group.

The module uses the shared statistical utility from:

```text
src/Utility.py
```

---

## `two_sample_t_test.py`

Responsible for the inferential statistical comparison between the two groups.

It performs a:

> **Welch two-sample, two-sided t-test**

It also calculates the Welch-Satterthwaite degrees of freedom and creates:

```text
t_distribution.png
```

---

# `src/Utility.py`

This file contains reusable statistical functions used by the project.

For Question 1, it provides the confidence interval calculation used by:

```text
src/task1/confidence_interval.py
```

---

# Question 1 Data Wrangling

The raw dataset contains **1,039 player records**.

The analysis identifies the actual FBref header within the CSV and then processes the player data.

### Required columns

```text
Player
Pos
Squad
Age
Sh/90
```

### Cleaning steps

1. Identify the actual FBref header.
2. Clean column names.
3. Clean player names.
4. Clean player positions.
5. Clean squad names.
6. Convert Age to numeric.
7. Convert Shots/90 to numeric.
8. Remove invalid records.
9. Identify attacking players.

For the current dataset:

```text
Original records: 1039
Records removed during cleaning: 0
Attacking players found: 275
```

---

# Definition of Attacking Players

For Question 1, attacking players are identified using the FBref `Pos` field.

Players whose position contains:

```text
FW
```

are included.

This can include positions such as:

```text
FW
FWMF
MFFW
```

Goalkeepers and other non-attacking positions are excluded.

---

# Age Groups

The analysis uses two age groups.

## Under 25

```text
Age < 25
```

## Age 28+

```text
Age >= 28
```

Players aged 25, 26 and 27 are not included in either comparison group.

For the current dataset:

```text
Under 25 attacking players available: 69
Age 28+ attacking players available: 123
```

---

# Sampling

A reproducible random sampling method is used.

### Random seed

```text
137
```

### Final sample

```text
Under 25 = 10
Age 28+   = 25
Total     = 35
```

The processed dataset is saved as:

```text
data/processed/processed1.csv
```

From the original 1,039 records, 35 records are used for the final analysis.

```text
Records excluded from original dataset: 1004
```

---

# Descriptive Statistics Results

The current Question 1 sample produced the following results.

| Statistic          | Under 25 | Age 28+ |
| ------------------ | -------: | ------: |
| Sample size        |       10 |      25 |
| Mean               |    4.268 |   4.307 |
| Median             |    1.880 |   1.740 |
| Minimum            |    0.000 |   0.000 |
| Maximum            |   22.500 |  45.000 |
| Range              |   22.500 |  45.000 |
| Variance           |   44.882 |  83.698 |
| Standard deviation |    6.699 |   9.149 |
| Q1                 |    1.205 |   0.620 |
| Q3                 |    4.355 |   3.310 |
| IQR                |    3.150 |   2.690 |

The sample means are very similar:

```text
Under 25: 4.268 Shots/90
Age 28+:  4.307 Shots/90
```

---

# Confidence Interval Results

The 95% confidence intervals are:

| Age Group |  Mean | 95% Confidence Interval |
| --------- | ----: | ----------------------: |
| Under 25  | 4.268 |         -0.524 to 9.060 |
| Age 28+   | 4.307 |          0.531 to 8.084 |

The confidence intervals are used together with the t-test to assess whether there is evidence of a difference between the two population means.

---

# Welch Two-Sample t-Test

A Welch two-sample t-test is used because the two groups have different sample sizes and different sample variances.

The test is two-sided.

## Null Hypothesis (H0)

> There is no difference in mean Shots/90 between attacking players under 25 and attacking players aged 28+.

## Alternative Hypothesis (H1)

> There is a difference in mean Shots/90 between attacking players under 25 and attacking players aged 28+.

### Significance level

```text
α = 0.05
```

### Results

```text
t-statistic = -0.014
Degrees of freedom = 22.698
p-value = 0.9889
```

### Decision

```text
Fail to reject H0
```

Because:

```text
0.9889 > 0.05
```

there is not enough statistical evidence to reject the null hypothesis.

---

# Question 1 Conclusion

Based on the current sample and Welch two-sample t-test:

> **There is not enough statistical evidence to conclude that the mean Shots/90 differs between attacking players under 25 and attacking players aged 28+.**

The sample means are very close:

```text
Under 25 = 4.268
Age 28+  = 4.307
```

The p-value of **0.9889** is considerably greater than the significance level of **0.05**.

Therefore, the null hypothesis is **not rejected**.

Failing to reject the null hypothesis does not prove that the two population means are exactly equal. It means that the current sample does not provide sufficient statistical evidence for a statistically significant difference.

---

# Running the Analysis

First, navigate to the project root:

```bash
cd "/home/hemanta/Documents/CDU/Foundations of Data Science/Final Assesment/sydney-group-13-fifa2026"
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run Question 1:

```bash
python scripts/task1.py
```

Alternatively, from the `scripts` directory:

```bash
cd scripts
python task1.py
```

---

# Expected Output

After successfully running the script, the following files are generated or updated:

### Processed dataset

```text
data/processed/processed1.csv
```

### Results report

```text
docs/task1.md
```

### Histogram

```text
figures/task1/histogram.png
```

### Boxplot

```text
figures/task1/boxplot.png
```

### t-distribution

```text
figures/task1/t_distribution.png
```

### Jupyter Notebook

```text
notebooks/task1.ipynb
```

The three graphs are displayed together after the complete analysis has finished.

---

# Requirements

The main Python libraries used for Question 1 include:

```text
pandas
numpy
scipy
matplotlib
```

The project dependencies are listed in:

```text
requirements.txt
```

Install them with:

```bash
pip install -r requirements.txt
```

---

# Generated Output Summary

| Output                        | Location                              |
| ----------------------------- | ------------------------------------- |
| Raw dataset                   | `data/raw/raw1.csv`                   |
| Processed dataset             | `data/processed/processed1.csv`       |
| Question 1 report             | `docs/task1.md`                       |
| Histogram                     | `figures/task1/histogram.png`         |
| Boxplot                       | `figures/task1/boxplot.png`           |
| t-distribution                | `figures/task1/t_distribution.png`    |
| Question 1 script             | `scripts/task1.py`                    |
| Question 2 script             | `scripts/task2.py`                    |
| Data wrangling module         | `src/task1/data_wrangling.py`         |
| Data preparation module       | `src/task1/data_preparation.py`       |
| Descriptive statistics module | `src/task1/descriptive_statistics.py` |
| Confidence interval module    | `src/task1/confidence_interval.py`    |
| t-test module                 | `src/task1/two_sample_t_test.py`      |
| Statistical utility           | `src/Utility.py`                      |
| Jupyter Notebook              | `notebooks/task1.ipynb`               |

---

# Team Question Summary

| Question | Analytical Focus                 | Comparison                            | Status          |
| -------- | -------------------------------- | ------------------------------------- | --------------- |
| **Q1**   | Shots/90 and age                 | Under 25 vs Age 28+ attacking players | **Completed**   |
| **Q2**   | Tackles/90 and position          | Defenders vs midfielders/forwards     | To be completed |
| **Q3**   | Fouls/90 and starting percentage | Started ≥50% vs <50%                  | To be completed |
| **Q4**   | SoT% and possession              | Possession >55% vs ≤55%               | To be completed |

---

# Question 1 Ownership

**Question:** Q1 - Shots/90 and Age

**Completed by:** Hemanta Adhikari

**Student ID:** s403355

**Main script:**

```text
scripts/task1.py
```

**Modules:**

```text
src/task1/
├── confidence_interval.py
├── data_preparation.py
├── data_wrangling.py
├── descriptive_statistics.py
└── two_sample_t_test.py
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

**Results:**

```text
docs/task1.md
```

**Visualisations:**

```text
figures/task1/
```

**Notebook:**

```text
notebooks/task1.ipynb
```

---

# Repository Information

**Repository:** `sydney-group-13-fifa2026`

**Project:** FIFA World Cup 2026 Analytics

**Unit:** HIT137 Foundations of Data Science

**Assessment:** Final Assessment

**Question 1:** Shots/90 and Age

**Question 1 Student:** Hemanta Adhikari

**Student ID:** s403355

**Data Source:** FBref - Player Shooting Statistics

**Question 1 Status:** Completed
