"""
inspect_data.py
================
Quick data quality inspection for the restaurant dataset before visualization.

Reads:   data/du_lieu_nha_hang_t11_2025.csv
Outputs: shape, columns, dtypes, head, numeric summary stats,
         missing-value counts, and duplicate-row counts.
"""

import pandas as pd

# ----------------------------------------------------------------------
# 1. CONFIGURATION
# ----------------------------------------------------------------------
CSV_PATH = r"C:\document\Study documents\Data visualizaion\data\du_lieu_nha_hang_t11_2025.csv"

# Display settings so wide frames don't get truncated
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)
pd.set_option("display.float_format", "{:,.2f}".format)

# ----------------------------------------------------------------------
# 2. LOAD THE DATASET
# ----------------------------------------------------------------------
print("=" * 70)
print("LOADING DATASET")
print("=" * 70)

# The file begins with a UTF-16 LE BOM (0xFF 0xFE), so it must be read as UTF-16.
# A simple BOM sniff lets the script handle either UTF-8 or UTF-16 transparently.
with open(CSV_PATH, "rb") as f:
    raw = f.read(2)
enc = "utf-16" if raw == b"\xff\xfe" or raw == b"\xfe\xff" else "utf-8"

df = pd.read_csv(CSV_PATH, encoding=enc)
print(f"Detected encoding: {enc}\n")
print(f"Dataset loaded successfully from:\n  {CSV_PATH}\n")

# ----------------------------------------------------------------------
# 3. SHAPE (rows x columns)
# ----------------------------------------------------------------------
print("=" * 70)
print("DATASET SHAPE")
print("=" * 70)
print(f"Rows    : {df.shape[0]:,}")
print(f"Columns : {df.shape[1]}\n")

# ----------------------------------------------------------------------
# 4. COLUMN NAMES & DATA TYPES
# ----------------------------------------------------------------------
print("=" * 70)
print("COLUMN NAMES & DATA TYPES")
print("=" * 70)
print(df.dtypes.to_string())
print()

# ----------------------------------------------------------------------
# 5. FIRST FEW ROWS
# ----------------------------------------------------------------------
print("=" * 70)
print("FIRST 5 ROWS")
print("=" * 70)
print(df.head())
print()

# ----------------------------------------------------------------------
# 6. SUMMARY STATISTICS FOR NUMERIC COLUMNS
# ----------------------------------------------------------------------
print("=" * 70)
print("SUMMARY STATISTICS (NUMERIC COLUMNS)")
print("=" * 70)
numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
if numeric_cols:
    print(df[numeric_cols].describe().to_string())
else:
    print("No numeric columns found in the dataset.")
print()

# ----------------------------------------------------------------------
# 7. MISSING VALUES
# ----------------------------------------------------------------------
print("=" * 70)
print("MISSING VALUES")
print("=" * 70)
missing = df.isna().sum()
missing_cols = missing[missing > 0]
if not missing_cols.empty:
    total_missing = missing_cols.sum()
    print(f"Total missing cells: {total_missing:,} "
          f"({total_missing / (df.shape[0] * df.shape[1]):.2%} of all cells)\n")
    print("Columns with missing values:")
    for col, count in missing_cols.items():
        print(f"  {col:<30} {count:>8,}  ({count / df.shape[0]:.2%})")
else:
    print("No missing values found in any column.")
print()

# ----------------------------------------------------------------------
# 8. DUPLICATE ROWS
# ----------------------------------------------------------------------
print("=" * 70)
print("DUPLICATE ROWS")
print("=" * 70)
dup_count = df.duplicated().sum()
print(f"Exact duplicate rows: {dup_count:,} "
      f"({dup_count / df.shape[0]:.2%} of all rows)")
print()

print("=" * 70)
print("INSPECTION COMPLETE")
print("=" * 70)
