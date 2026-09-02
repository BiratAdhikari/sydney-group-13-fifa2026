import os
import pandas as pd


def data_wrangling(raw_file):
    # --------------------------------------------------------------------------
    # Check raw dataset.
    # --------------------------------------------------------------------------
    if not os.path.exists(raw_file):
        raise FileNotFoundError(
            "\nRaw dataset was not found.\n\n"
            f"Expected location:\n{raw_file}\n\n"
            "Please make sure raw1.csv is inside data/raw/."
        )

    # --------------------------------------------------------------------------
    # Read raw CSV as text.
    # --------------------------------------------------------------------------
    with open(raw_file, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()

    # --------------------------------------------------------------------------
    # Find actual FBref header.
    # --------------------------------------------------------------------------
    header_line_number = None

    for i, line in enumerate(lines):
        clean_line = line.strip()

        if (
            clean_line.startswith("Rk,")
            and "Player" in clean_line
            and "Pos" in clean_line
            and "Age" in clean_line
            and "Sh/90" in clean_line
        ):
            header_line_number = i
            break

    # --------------------------------------------------------------------------
    # Stop if header cannot be found.
    # --------------------------------------------------------------------------
    if header_line_number is None:
        print("\nERROR: The real FBref table header could not be found.")
        print("\nThe first 10 lines of the file are:")

        for line in lines[:10]:
            print(line.strip())

        raise ValueError("Could not find the FBref table header.")

    print(
        f"\nActual FBref header found at CSV line: "
        f"{header_line_number + 1}"
    )

    # --------------------------------------------------------------------------
    # Read CSV from actual header.
    # --------------------------------------------------------------------------
    df = pd.read_csv(raw_file, skiprows=header_line_number)

    # --------------------------------------------------------------------------
    # Clean column names.
    # --------------------------------------------------------------------------
    df.columns = (
        df.columns.astype(str)
        .str.replace(r"[\r\n]", "", regex=True)
        .str.strip()
    )

    print("\nColumns found:")
    print(df.columns.tolist())

    original_records = len(df)

    print(f"\nOriginal number of records: {original_records}")

    # ==========================================================================
    # CHECK REQUIRED COLUMNS
    # ==========================================================================
    required_columns = ["Player", "Pos", "Squad", "Age", "Sh/90"]

    missing_columns = [
        column for column in required_columns if column not in df.columns
    ]

    if missing_columns:
        print("\nERROR: Required columns are missing:")
        print(missing_columns)
        print("\nAvailable columns:")
        print(df.columns.tolist())
        raise ValueError("The required FBref columns are missing.")

    # ==========================================================================
    # CLEAN DATA VALUES
    # ==========================================================================
    df["Player"] = df["Player"].astype(str).str.strip()

    df["Pos"] = df["Pos"].astype(str).str.strip()

    # Remove FBref country-code prefix.
    df["Squad"] = (
        df["Squad"]
        .astype(str)
        .str.strip()
        .str.split(" ", n=1)
        .str[-1]
    )

    # Convert Age.
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

    # Convert Shots/90.
    df["Sh/90"] = pd.to_numeric(df["Sh/90"], errors="coerce")

    # ==========================================================================
    # REMOVE INVALID RECORDS
    # ==========================================================================
    before_cleaning = len(df)

    df = df.dropna(
        subset=["Player", "Pos", "Age", "Sh/90"]
    ).copy()

    after_cleaning = len(df)

    records_removed = before_cleaning - after_cleaning

    print(f"\nRecords removed during cleaning: {records_removed}")

    # ==========================================================================
    # FILTER ATTACKING PLAYERS
    # ==========================================================================
    attackers = df[
        df["Pos"].str.contains("FW", case=False, na=False)
    ].copy()

    print(f"\nAttacking players found: {len(attackers)}")

    # ==========================================================================
    # CREATE AGE GROUPS
    # ==========================================================================
    under25_all = attackers[attackers["Age"] < 25].copy()
    age28plus_all = attackers[attackers["Age"] >= 28].copy()

    print(
        f"\nUnder 25 attacking players available: "
        f"{len(under25_all)}"
    )

    print(
        f"Age 28+ attacking players available: "
        f"{len(age28plus_all)}"
    )

    return {
        "df": df,
        "attackers": attackers,
        "under25_all": under25_all,
        "age28plus_all": age28plus_all,
        "original_records": original_records,
        "records_removed": records_removed,
    }
