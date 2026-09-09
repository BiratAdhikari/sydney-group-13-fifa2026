import pandas as pd


def data_preparation(
    df, processed_file, starter_threshold=0.50, sample_size=35, random_state=42
):
    print("\n" + "=" * 60)
    print("2. DATA PREPARATION AND GROUPING")
    print("=" * 60)

    # Define Starter Ratio (Starts / MP)
    df["start_ratio"] = df["Starts"] / df["MP"]
    df["group"] = df["start_ratio"].apply(
        lambda r: "Starter" if r >= starter_threshold else "Non-Starter"
    )

    # Keep a reproducible, proportionally stratified sample.  Sampling after
    # grouping ensures both comparison groups remain represented in the 35
    # records used for the analysis.
    if sample_size is not None:
        if sample_size < 4:
            raise ValueError("sample_size must be at least 4 to compare both groups.")
        if sample_size > len(df):
            raise ValueError(
                f"sample_size ({sample_size}) cannot exceed available records ({len(df)})."
            )

        group_counts = df["group"].value_counts()
        if len(group_counts) != 2:
            raise ValueError("Both Starter and Non-Starter records are required.")

        non_starter_size = round(sample_size * group_counts["Non-Starter"] / len(df))
        non_starter_size = max(2, min(non_starter_size, group_counts["Non-Starter"]))
        starter_size = sample_size - non_starter_size
        if starter_size > group_counts["Starter"]:
            raise ValueError("Not enough Starter records for the requested sample size.")

        starters = df[df["group"] == "Starter"].sample(
            n=starter_size, random_state=random_state
        )
        non_starters = df[df["group"] == "Non-Starter"].sample(
            n=non_starter_size, random_state=random_state
        )
        df = (
            pd.concat([starters, non_starters])
            .sort_index()
            .reset_index(drop=True)
        )

    # Split the final sampled dataset into groups
    starters = df[df["group"] == "Starter"].copy()
    non_starters = df[df["group"] == "Non-Starter"].copy()

    # Save Processed Dataset
    df.to_csv(processed_file, index=False)

    print(f"Total processed records saved to: {processed_file} ({len(df)} records)")
    print(f"Starters (Starts/MP >= 50%): {len(starters)}")
    print(f"Non-Starters (Starts/MP < 50%): {len(non_starters)}")

    return df, starters, non_starters
