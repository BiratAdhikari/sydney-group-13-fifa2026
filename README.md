# sydney-group-13-fifa2026
# Sydney Group 13 - FIFA World Cup 2026 Analytics (Objective 1)

This repository contains the code, data, and documentation for Objective 1 of the FIFA World Cup 2026 data analytics project. Our team is investigating four distinct analytic questions using data sourced from FIFA, FBref, and The Stats Don't Lie.

## Team Members
* [Member 1 Name](GitHub Profile Link) - Task 1
* [Member 2 Name](GitHub Profile Link) - Task 2
* [Member 3 Name](GitHub Profile Link) - Task 3
* [Reviewer Name] (GitHub Profile Link) - Task 4 & Lead PR Reviewer

---

## 📂 Folder Structure & File Nomenclature

We use a modular structure to separate raw data, processing scripts, and final outputs. All files and folders must adhere to **snake_case** (lowercase words separated by underscores).

```text
sydney-group-13-fifa2026/
├── .gitignore                 # System files and raw data exclusions
├── README.md                  # Project documentation and nomenclature rules
├── requirements.txt           # Python dependencies
├── data/                      
│   ├── raw/                   # Unmodified CSV files (e.g., fbref_squad_stats.csv)
│   └── processed/             # Cleaned CSV files (e.g., task_1_cleaned_players.csv)
├── docs/                      # Markdown reports detailing the  steps for each task
│   ├── task_1_shots_age.md
│   ├── task_2_tackles.md
│   ├── task_3_fouls.md
│   └── task_4_possession.md
├── figures/                   # Visualizations generated from descriptive statistics
│   ├── task_1_shots_boxplot.png
│   └── task_4_sot_histogram.png
├── notebooks/                 # Jupyter Notebooks for analysis
│   └── task_1_shots_age.ipynb
├── scripts/                   # Python scripts for analysis
│   └── task_4_possession.py
└── src/                       # Shared helper functions
    ├── data_cleaning.py       
    └── stat_tests.py