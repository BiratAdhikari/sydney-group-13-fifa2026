<!--
==============================================================================
HIT140 Foundations of Data Science Assessment - Question 3
Student Name : John Karki
Student ID   : s403518

Topic        : Fouls/90 Analysis - Starters vs. Non-Starters
               World Cup 2026 Player Discipline Analysis

Data Source  : FBref 2026 World Cup Player Standard & Misc Statistics
==============================================================================
-->

# Task 3 Results: Fouls per 90 (Starters vs Non-Starters)

## 1. Summary Table

| Metric | Starters | Non-Starters |
|---|---:|---:|
| Sample Size (n) | 31 | 4 |
| Mean Fouls/90 | 1.183 | 1.816 |
| Std Dev | 0.766 | 0.625 |
| 95% CI | [0.902, 1.464] | [0.822, 2.810] |

`processed3.csv` contains a reproducible, proportionally stratified sample of
35 valid player records (`random_state=42`): 31 starters and 4 non-starters.

## 2. Inferential Statistics

- **t-statistic**: -1.855
- **Degrees of Freedom**: 4.263
- **p-value**: 0.1327
- **Decision**: Fail to Reject H0

### Conclusion
Although the non-starter sample mean is higher, this 35-record sample does not
provide statistically significant evidence of a difference in mean Fouls/90
between starters and non-starters at the 5% significance level.
