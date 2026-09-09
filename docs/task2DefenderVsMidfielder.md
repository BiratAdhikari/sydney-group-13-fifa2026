<!--
==============================================================================
HIT140 Foundations of Data Science Assessment - Question 2
Student Name : Birat Adhikari
Student Id   : S403356

Topic        : Tackles Won per 90 Analysis - Defenders vs. Midfielders and Forwards
			   World Cup 2026 Player Tackling Analysis

Research Question:
			   Do defenders win significantly more tackles per 90 minutes
			   than midfielders and forwards?

Data Source  : FBref 2026 World Cup Player Standard Statistics & Misc Statistics
==============================================================================
-->

# Task 2 Results: Tackles Won per 90 (Defenders vs Midfielders and Forwards)

## 1. Descriptive Statistics

The analysis used a random sample of 40 players. Players were classified into
two tactical roles: `Defensive` and `Attacking`, where the attacking group
contains midfielders and forwards.

| Tactical Role | Sample Size (n) | Mean Tackles Won per 90 | Maximum Tackles Won per 90 |
|---|---:|---:|---:|
| Attacking | 27 | 1.231 | 10.000 |
| Defensive | 13 | 1.846 | 20.000 |

The overall sample mean was **1.43 Tackles Won per 90**, with a 95% confidence
interval of **[0.33, 2.54]**.

## 2. Detected Outliers

Outliers were identified using the interquartile range (IQR) method.

| Player | Squad | Tactical Role | Tackles Won per 90 |
|---|---|---|---:|
| Leo Østigård | no Norway | Defensive | 1.875 |
| Mohammad Abu Hasheesh | jo Jordan | Defensive | 20.000 |
| Keisuke Gotō | jp Japan | Attacking | 10.000 |

## 3. Inferential Statistics

A Welch two-sample t-test was used to compare Tackles Won per 90 between the
defensive and attacking groups.

- **t-statistic**: 0.3926
- **p-value**: 0.7007
- **Decision**: Fail to reject H0

### Conclusion

The p-value of 0.7007 is greater than the 0.05 significance level. Therefore,
there is no statistically significant evidence that defenders win more tackles
per 90 minutes than midfielders and forwards in this sample. Although the
defensive group had a higher sample mean than the attacking group, the observed
difference was not statistically significant.
