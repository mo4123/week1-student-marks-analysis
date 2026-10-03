# Week 1 Project — Student Marks Dataset Analysis

## Objective

Use Pandas and NumPy to clean a student-marks dataset and calculate average, minimum, and maximum scores.

## Dataset

Download `StudentsPerformance.csv` from the [Students Performance in Exams dataset on Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams).

Place it here:

```text
data/StudentsPerformance.csv
```

The official dataset has eight columns: gender, race/ethnicity, parental level of education, lunch, test preparation course, math score, reading score, and writing score.

## Installation

Open PowerShell in this project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the analysis

Script:

```powershell
python student_marks_analysis.py
```

Notebook:

```powershell
jupyter notebook student_marks_analysis.ipynb
```

## Cleaning decisions

- Remove duplicate rows.
- Convert the three score columns to numeric values.
- Treat scores outside 0–100 as invalid.
- Fill missing categorical values with `Unknown`.
- Fill missing or invalid scores using the median of the corresponding subject.
- Calculate every student's average using NumPy.

## Generated results

The script creates:

```text
results/cleaned_student_marks.csv
results/cleaning_log.csv
results/score_summary.csv
results/gender_summary.csv
results/preparation_summary.csv
results/top_students.csv
```

## Submission checklist

- Add your name and registration number to `PROJECT_REPORT.md` and the notebook.
- Add `StudentsPerformance.csv` to the `data` folder.
- Run all notebook cells.
- Confirm that all result tables appear.
- Update the findings section using your actual calculated values.
- Submit the notebook, report, script, and results requested by your instructor.

## Certificate note

An official course certificate must be issued by the course or training provider. This project package is evidence of assignment completion, but it is not an official certificate.
