import csv
import os
import pandas as pd


def load_and_clean_csv(file_path):
    """
    Parses FBref CSV files by filtering out top metadata rows,
    identifying column headers, and mapping metrics properly.
    """
    valid_rows = []

    # Read raw lines with csv reader to bypass metadata lines with inconsistent column counts
    with open(file_path, "r", encoding="utf-8-sig", errors="ignore") as f:
        reader = csv.reader(f)
        for row in reader:
            # Skip empty rows or single-column metadata titles
            if len(row) > 5:
                valid_rows.append(row)

    if not valid_rows:
        raise ValueError(f"No valid tabular data found in {file_path}")

    # Find the header row that contains 'Player' or 'Player' in position 1
    header_idx = None
    for idx, row in enumerate(valid_rows):
        cleaned_row = [str(c).strip().replace("\ufeff", "") for c in row]
        if "Player" in cleaned_row:
            header_idx = idx
            break

    if header_idx is not None:
        # Construct DataFrame using detected header row
        headers = [str(c).strip().replace("\ufeff", "") for c in valid_rows[header_idx]]
        data = valid_rows[header_idx + 1:]
        df = pd.DataFrame(data, columns=headers)
    else:
        # Fallback: Headerless setup — assume row 0 is first data row
        headers = [
            "Rk", "Player", "Pos", "Squad", "Age", "Born",
            "MP", "Starts", "Min", "90s"
        ]
        df = pd.DataFrame(valid_rows)
        # Rename available leading columns
        col_rename = {i: name for i, name in enumerate(headers) if i < len(df.columns)}
        df = df.rename(columns=col_rename)

        # If 'Fls' exists in the table (usually column index 11 or 12 in Misc stats)
        if 11 in df.columns and "Fls" not in df.columns:
            df = df.rename(columns={11: "Fls"})

    # Clean whitespace in column names and values
    df.columns = [str(c).strip() for c in df.columns]

    if "Player" in df.columns:
        df["Player"] = df["Player"].astype(str).str.strip()
        df = df[df["Player"] != "Player"].copy()

    return df


def merge_raw_files(standard_file, misc_file):
    """
    Merges FBref standard and misc raw CSV files on Player and Squad columns.
    """
    if not os.path.exists(standard_file) or not os.path.exists(misc_file):
        raise FileNotFoundError("One or both raw CSV input files are missing.")

    std_df = load_and_clean_csv(standard_file)
    misc_df = load_and_clean_csv(misc_file)

    # Standardize column keys
    for df in [std_df, misc_df]:
        if "Squad" not in df.columns:
            match = [c for c in df.columns if "squad" in str(c).lower()]
            if match:
                df.rename(columns={match[0]: "Squad"}, inplace=True)

    # Inner join on key identifiers
    merged_df = pd.merge(
        std_df,
        misc_df,
        on=["Player", "Squad"],
        how="inner",
        suffixes=("", "_misc")
    )

    return merged_df
