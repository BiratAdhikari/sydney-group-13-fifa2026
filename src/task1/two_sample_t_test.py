import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


def t_test(
    under25,
    age28plus,
    s1,
    n1,
    s2,
    n2,
    alpha,
    t_distribution_file
):
    print("\n" + "=" * 60)
    print("6. INFERENTIAL STATISTICS - TWO-SAMPLE T-TEST")
    print("=" * 60)

    print("\nNull hypothesis (H0):")
    print(
        "There is no difference in mean Shots/90 "
        "between attacking players under 25 and "
        "attacking players aged 28+."
    )

    print("\nAlternative hypothesis (H1):")
    print(
        "There is a difference in mean Shots/90 "
        "between attacking players under 25 and "
        "attacking players aged 28+."
    )

    print(f"\nSignificance level: {alpha}")

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

    print(f"\nt-statistic: {t_statistic:.3f}")
    print(f"Degrees of freedom: {welch_df:.3f}")
    print(f"p-value: {p_value:.4f}")

    # ==========================================================================
    # DECISION
    # ==========================================================================
    if p_value < alpha:
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

    print(f"\nDecision: {decision}")
    print(f"\nConclusion:\n{conclusion}")

    # ==========================================================================
    # T-DISTRIBUTION GRAPH
    # ==========================================================================
    print("\n" + "=" * 60)
    print("7. T-DISTRIBUTION VISUALISATION")
    print("=" * 60)

    critical_t = st.t.ppf(
        1 - alpha / 2,
        welch_df
    )

    # Create t-distribution range.
    x = np.linspace(-5, 5, 500)

    y = st.t.pdf(x, welch_df)

    print("\nCreating t-distribution graph...")

    plt.figure(figsize=(10, 6))

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

    plt.xlabel("t")
    plt.ylabel("Probability density")
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        t_distribution_file,
        dpi=300,
        bbox_inches="tight"
    )

    print(
        f"T-distribution graph saved to:\n"
        f"{t_distribution_file}"
    )

    # plt.show()

    return {
        "t_statistic": t_statistic,
        "p_value": p_value,
        "welch_df": welch_df,
        "critical_t": critical_t,
        "decision": decision,
        "conclusion": conclusion,
    }
