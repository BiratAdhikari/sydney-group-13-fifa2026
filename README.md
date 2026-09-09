# Sydney Group 13 - FIFA World Cup 2026 Analytics

This repository contains our **HIT137 Objective 1** FIFA World Cup 2026 data analysis project. The project investigates four analytical questions using football data from **FIFA, FBref, and The Stats Don't Lie**.

## Team Members and Analytical Questions

| Task       | Student           | Student ID  | Analytical Question                                                                                                                     | Status        |
| ---------- | ----------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Task 1** | Hemanta Adhikari  | **s403355** | Is there a statistically significant difference in Shots/90 between attacking players under 25 and attacking players aged 28+?          | ✅ PASS        |
| **Task 2** | Birat Adhikari    | **s403356**         | Do defenders win significantly more tackles per 90 minutes than midfielders and forwards?                                               | ✅ PASS        |
| **Task 3** | John Karki        | **s403518**         | Do players who started at least 50% of their team's matches commit significantly more Fouls/90 than players who started fewer than 50%? | ✅ PASS        |
| **Task 4** | Muhammad Hussnain | **s406259**        | Do teams with average possession above 55% have a significantly higher SoT% than teams with possession of 55% or below?                 | ✅ PASS   |

## Required Analytical Steps

Each task must complete all six steps:

1. **Analytic question formulation**
2. **Data wrangling**
3. **Data preparation and sampling**
4. **Descriptive statistics**
5. **Inferential statistics – Confidence interval**
6. **Inferential statistics – One-Sample t-Test OR Two-Sample t-Test**

A task is **PASS** only when all six required steps are completed.

## Project Structure

```text
sydney-group-13-fifa2026/
├── data/
│   ├── raw/
│   │   ├── task1/
│   │   ├── task2DefenderVsMidfielderRaw/
│   │   ├── task3/
│   │   └── task4/
│   │
│   └── processed/
│       ├── task1/
│       ├── task2DefenderVsMidfielderProcessed/
│       ├── task3/
│       └── task4/
│
├── docs/
│   ├── task1.md
│   ├── task2DefenderVsMidfielder.md
│   ├── task3.md
│   └── task4.md
│
├── figures/
│   ├── task1/
│   ├── task2DefenderVsMidfielderFigures/
│   ├── task3/
│   └── task4/
│
├── scripts/
│   ├── task1.py
│   ├── defenderVsMidfielderTask2.py
│   ├── task3.py
│   └── task4.py
│
├── src/
│   ├── task1/
│   ├── defenderVsMidfielderTask2/
│   ├── task3/
│   ├── task4/
│   └── Utility.py
│
├── README.md
└── requirements.txt
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Go to the scripts folder:

```bash
cd scripts
```

Run the task you want:

```bash
python3 task1.py
python3 defenderVsMidfielderTask2.py
python3 task3.py
python3 task4.py
```

## Statistical Analysis

The project uses:

* Descriptive statistics
* 95% Confidence Interval
* One-Sample or Two-Sample t-Test
* Data visualisation
* Statistical interpretation

The significance level is **α = 0.05**.

## Data Sources

* FIFA
* FBref
* The Stats Don't Lie

## Repository Maintenance

Python-generated files should not be committed:

```text
__pycache__/
*.pyc
```

Add these files to `.gitignore`.
