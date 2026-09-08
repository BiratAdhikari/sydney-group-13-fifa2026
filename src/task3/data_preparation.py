import pandas as pd


def data_preparation(df, processed_file, starter_threshold=0.50):
    print("\n" + "=" * 60)
    print("2. DATA PREPARATION AND GROUPING")
    print("=" * 60)

    # Define Starter Ratio (Starts / MP)
    df["start_ratio"] = df["Starts"] / df["MP"]
    df["group"] = df["start_ratio"].apply(
        lambda r: "Starter" if r >= starter_threshold else "Non-Starter"
    )

    # Split Groups
    starters = df[df["group"] == "Starter"].copy()
    non_starters = df[df["group"] == "Non-Starter"].copy()

    # Save Processed Dataset
    df.to_csv(processed_file, index=False)

    print(f"Total processed records saved to: {processed_file}")
    print(f"Starters (Starts/MP >= 50%): {len(starters)}")
    print(f"Non-Starters (Starts/MP < 50%): {len(non_starters)}")

    return df, starters, non_starters
