import pandas as pd


def data_preparation(
    under25_all,
    age28plus_all,
    original_records,
    filtered_file,
    random_seed,
    total_sample_size,
    under25_sample_size,
    age28plus_sample_size,
):
    print("\n" + "=" * 60)
    print("2. DATA PREPARATION AND SAMPLING")
    print("=" * 60)

    print("\nPopulation:")
    print(
        "All attacking players in the supplied "
        "FIFA World Cup 2026 player dataset."
    )

    print("\nSampling method:")
    print("Random sampling with a fixed random seed.")

    print(f"\nRandom seed: {random_seed}")

    # ==========================================================================
    # CHECK SAMPLE AVAILABILITY
    # ==========================================================================
    if len(under25_all) < under25_sample_size:
        raise ValueError(
            "There are not enough Under 25 attacking players."
        )

    if len(age28plus_all) < age28plus_sample_size:
        raise ValueError(
            "There are not enough Age 28+ attacking players."
        )

    # ==========================================================================
    # SELECT REPRODUCIBLE SAMPLE
    # ==========================================================================
    under25_sample = under25_all.sample(
        n=under25_sample_size,
        random_state=random_seed
    )

    age28plus_sample = age28plus_all.sample(
        n=age28plus_sample_size,
        random_state=random_seed
    )

    # ==========================================================================
    # COMBINE GROUPS
    # ==========================================================================
    filtered_df = pd.concat(
        [under25_sample, age28plus_sample],
        ignore_index=True
    )

    # Shuffle the final sample.
    filtered_df = filtered_df.sample(
        frac=1,
        random_state=random_seed
    ).reset_index(drop=True)

    # ==========================================================================
    # VERIFY SAMPLE
    # ==========================================================================
    if len(filtered_df) != total_sample_size:
        raise ValueError(
            "The filtered dataset does not contain exactly 35 records."
        )

    # ==========================================================================
    # SAVE PROCESSED DATA
    # ==========================================================================
    filtered_df.to_csv(filtered_file, index=False)

    print(f"\nRecords used for analysis: {len(filtered_df)}")
    print(f"Records excluded from original dataset: {original_records - len(filtered_df)}")
    print("\nProcessed dataset saved to:")
    print(filtered_file)

    # ==========================================================================
    # RELOAD PROCESSED DATA
    # ==========================================================================
    df = pd.read_csv(filtered_file)

    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df["Sh/90"] = pd.to_numeric(df["Sh/90"], errors="coerce")

    # ==========================================================================
    # FINAL GROUPS
    # ==========================================================================
    under25 = df[df["Age"] < 25].copy()
    age28plus = df[df["Age"] >= 28].copy()

    print("\nFinal group sizes:")
    print(f"Under 25: {len(under25)}")
    print(f"Age 28+: {len(age28plus)}")

    return df, under25, age28plus
