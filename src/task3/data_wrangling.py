import pandas as pd
from src.task3.merge_files import merge_raw_files


def data_wrangling(standard_raw_file, misc_raw_file):
    print("\n" + "=" * 60)
    print("1. DATA WRANGLING")
    print("=" * 60)

    # 1. Merge raw exports using helper
    merged_df = merge_raw_files(standard_raw_file, misc_raw_file)
    original_records = len(merged_df)

    # 2. Coerce numeric types
    merged_df["90s"] = pd.to_numeric(merged_df["90s"], errors="coerce")
    merged_df["Fls"] = pd.to_numeric(merged_df["Fls"], errors="coerce")
    merged_df["Starts"] = pd.to_numeric(merged_df["Starts"], errors="coerce")
    merged_df["MP"] = pd.to_numeric(merged_df["MP"], errors="coerce")

    # 3. Drop missing values and calculate metric
    cleaned_df = merged_df.dropna(subset=["90s", "Fls", "Starts", "MP"]).copy()
    cleaned_df["fouls_per_90"] = cleaned_df["Fls"] / cleaned_df["90s"]

    # 4. Filter for minimum playing time threshold (>= 1.0 90s)
    filtered_df = cleaned_df[cleaned_df["90s"] >= 1.0].copy()
    records_removed = original_records - len(filtered_df)

    print(f"Original merged records: {original_records}")
    print(f"Records removed (< 1.0 90s or NaN): {records_removed}")
    print(f"Valid records remaining: {len(filtered_df)}")

    return {
        "df": filtered_df,
        "original_records": original_records,
        "records_removed": records_removed,
    }
