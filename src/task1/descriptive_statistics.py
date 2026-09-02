import numpy as np
import matplotlib.pyplot as plt


def describe_group(sample, label):
    arr = np.array(sample, dtype=float)

    n = len(arr)
    mean_v = arr.mean()
    median_v = np.median(arr)
    min_v = arr.min()
    max_v = arr.max()
    range_v = max_v - min_v
    variance_v = arr.var(ddof=1)
    std_v = arr.std(ddof=1)

    q1, q3 = np.percentile(arr, [25, 75])
    iqr_v = q3 - q1

    print(f"\n{label}")
    print("-" * 40)
    print(f"Sample size (n): {n}")
    print(f"Mean: {mean_v:.3f}")
    print(f"Median: {median_v:.3f}")
    print(f"Minimum: {min_v:.3f}")
    print(f"Maximum: {max_v:.3f}")
    print(f"Range: {range_v:.3f}")
    print(f"Variance: {variance_v:.3f}")
    print(f"Standard deviation: {std_v:.3f}")
    print(f"Q1: {q1:.3f}")
    print(f"Q3: {q3:.3f}")
    print(f"IQR: {iqr_v:.3f}")

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


def descriptive_statistics(under25, age28plus, histogram_file, boxplot_file):
    print("\n" + "=" * 60)
    print("3. DESCRIPTIVE STATISTICS")
    print("=" * 60)

    stats_u25 = describe_group(under25["Sh/90"], "Under 25")
    stats_28plus = describe_group(age28plus["Sh/90"], "Age 28+")

    print("\n" + "=" * 60)
    print("4. VISUALISATIONS")
    print("=" * 60)

    print("\nCreating histogram...")

    plt.figure(figsize=(10, 6))

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

    plt.title("Histogram of Shots/90 - Under 25 vs Age 28+")
    plt.xlabel("Shots per 90 minutes")
    plt.ylabel("Number of players")
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        histogram_file,
        dpi=300,
        bbox_inches="tight"
    )

    print(f"Histogram saved to:\n{histogram_file}")

    # plt.show()

    print("\nCreating boxplot...")

    plt.figure(figsize=(8, 6))

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

    plt.title("Boxplot of Shots/90 - Under 25 vs Age 28+")
    plt.ylabel("Shots per 90 minutes")
    plt.tight_layout()

    plt.savefig(
        boxplot_file,
        dpi=300,
        bbox_inches="tight"
    )

    print(f"Boxplot saved to:\n{boxplot_file}")

    # plt.show()

    return stats_u25, stats_28plus
