"""Week 1 project: analyze the Student Marks dataset with Pandas and NumPy."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


REQUIRED_COLUMNS = [
    "gender",
    "race/ethnicity",
    "parental level of education",
    "test preparation course",
    "math score",
    "reading score",
    "writing score",
]

SCORE_COLUMNS = ["math score", "reading score", "writing score"]
CATEGORY_COLUMNS = [
    "gender",
    "race/ethnicity",
    "parental level of education",
    "test preparation course",
]


def clean_dataset(csv_path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load the CSV, clean missing/invalid values, and return a cleaning log."""

    data = pd.read_csv(csv_path)
    data.columns = data.columns.str.strip()

    missing_columns = [column for column in REQUIRED_COLUMNS if column not in data.columns]
    if missing_columns:
        raise ValueError(
            "The CSV is missing these required columns: " + ", ".join(missing_columns)
        )

    original_rows = len(data)
    duplicate_rows = int(data.duplicated().sum())
    data = data.drop_duplicates().copy()

    for column in CATEGORY_COLUMNS:
        data[column] = data[column].astype("string").str.strip()
        data[column] = data[column].replace("", pd.NA)

    for column in SCORE_COLUMNS:
        data[column] = pd.to_numeric(data[column], errors="coerce")
        data.loc[~data[column].between(0, 100), column] = np.nan

    missing_before = data[REQUIRED_COLUMNS].isna().sum()

    for column in CATEGORY_COLUMNS:
        data[column] = data[column].fillna("Unknown")

    for column in SCORE_COLUMNS:
        median_score = data[column].median()
        if pd.isna(median_score):
            raise ValueError(f"'{column}' has no valid scores to use for cleaning.")
        data[column] = data[column].fillna(median_score)

    score_array = data[SCORE_COLUMNS].to_numpy(dtype=float)
    data["average score"] = np.round(np.mean(score_array, axis=1), 2)

    cleaning_log = pd.DataFrame(
        {
            "item": [
                "Original rows",
                "Duplicate rows removed",
                "Rows after cleaning",
                *[f"Missing/invalid values filled: {column}" for column in REQUIRED_COLUMNS],
            ],
            "value": [
                original_rows,
                duplicate_rows,
                len(data),
                *[int(missing_before[column]) for column in REQUIRED_COLUMNS],
            ],
        }
    )

    return data, cleaning_log


def analyze_dataset(data: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Create the statistical tables required for the assignment."""

    analyzed_columns = SCORE_COLUMNS + ["average score"]

    score_summary = (
        data[analyzed_columns]
        .agg(["mean", "min", "max"])
        .transpose()
        .rename(columns={"mean": "average", "min": "minimum", "max": "maximum"})
        .round(2)
    )

    gender_summary = (
        data.groupby("gender", dropna=False)[analyzed_columns]
        .mean()
        .round(2)
        .sort_index()
    )

    preparation_summary = (
        data.groupby("test preparation course", dropna=False)[analyzed_columns]
        .mean()
        .round(2)
        .sort_index()
    )

    top_students = data.nlargest(5, "average score")[
        ["gender", "race/ethnicity", *SCORE_COLUMNS, "average score"]
    ].reset_index(drop=True)

    return {
        "score_summary": score_summary,
        "gender_summary": gender_summary,
        "preparation_summary": preparation_summary,
        "top_students": top_students,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze the Student Marks dataset.")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/StudentsPerformance.csv"),
        help="Location of StudentsPerformance.csv",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results"),
        help="Folder where result CSV files will be saved",
    )
    args = parser.parse_args()

    if not args.input.exists():
        raise FileNotFoundError(
            f"Dataset not found: {args.input}\n"
            "Download StudentsPerformance.csv and place it in the data folder."
        )

    args.output.mkdir(parents=True, exist_ok=True)

    cleaned_data, cleaning_log = clean_dataset(args.input)
    tables = analyze_dataset(cleaned_data)

    cleaned_data.to_csv(args.output / "cleaned_student_marks.csv", index=False)
    cleaning_log.to_csv(args.output / "cleaning_log.csv", index=False)

    for name, table in tables.items():
        table.to_csv(args.output / f"{name}.csv")

    print("\nSTUDENT MARKS DATASET ANALYSIS")
    print("=" * 38)
    print("\nCleaning summary:")
    print(cleaning_log.to_string(index=False))
    print("\nAverage, minimum and maximum scores:")
    print(tables["score_summary"].to_string())
    print("\nAverage scores by gender:")
    print(tables["gender_summary"].to_string())
    print("\nAverage scores by test-preparation course:")
    print(tables["preparation_summary"].to_string())
    print("\nTop five students by average score:")
    print(tables["top_students"].to_string(index=False))
    print(f"\nResult files saved in: {args.output.resolve()}")


if __name__ == "__main__":
    main()
