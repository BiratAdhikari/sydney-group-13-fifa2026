from src.Utility import ci_mean


def confidence_interval(starters, non_starters):
    print("\n" + "=" * 60)
    print("4. INFERENTIAL STATISTICS - CONFIDENCE INTERVAL")
    print("=" * 60)

    # Starters
    (
        x_bar1,
        s1,
        n1,
        ci_low1,
        ci_upp1
    ) = ci_mean(starters["fouls_per_90"])

    print("\nStarters:")
    print(f"Mean: {x_bar1:.3f}")
    print(f"Standard deviation: {s1:.3f}")
    print(f"Sample size: {n1}")
    print(f"95% Confidence Interval: {ci_low1:.3f} to {ci_upp1:.3f}")

    # Non-Starters
    (
        x_bar2,
        s2,
        n2,
        ci_low2,
        ci_upp2
    ) = ci_mean(non_starters["fouls_per_90"])

    print("\nNon-Starters:")
    print(f"Mean: {x_bar2:.3f}")
    print(f"Standard deviation: {s2:.3f}")
    print(f"Sample size: {n2}")
    print(f"95% Confidence Interval: {ci_low2:.3f} to {ci_upp2:.3f}")

    return {
        "x_bar1": x_bar1,
        "s1": s1,
        "n1": n1,
        "ci_low1": ci_low1,
        "ci_upp1": ci_upp1,
        "x_bar2": x_bar2,
        "s2": s2,
        "n2": n2,
        "ci_low2": ci_low2,
        "ci_upp2": ci_upp2,
    }
