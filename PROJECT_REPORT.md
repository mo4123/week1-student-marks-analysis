# Week 1 Project Report: Student Marks Dataset Analysis

**Student name:** ____________________  
**Registration number:** ____________________  
**Submission date:** ____________________

## 1. Project objective

The objective of this project is to use Python, Pandas, and NumPy to load and clean a student-marks dataset, calculate students' average scores, and report the average, minimum, and maximum marks in mathematics, reading, and writing.

## 2. Dataset description

The project uses the `StudentsPerformance.csv` dataset from Kaggle. It contains student background information and scores for mathematics, reading, and writing. The analysis uses gender, race/ethnicity, parental level of education, test preparation course, and the three subject scores. The original dataset also contains a lunch column.

## 3. Tools used

- Python
- Pandas for loading, cleaning, grouping, and displaying data
- NumPy for calculating each student's average score
- Jupyter Notebook for presenting the analysis

## 4. Data-cleaning process

1. Column names were checked against the required columns.
2. Duplicate rows were removed.
3. Blank categorical values were replaced with `Unknown`.
4. Score values were converted to numeric form.
5. Scores outside the valid range of 0–100 were treated as missing.
6. Missing scores were filled with the median score for that subject.
7. A new `average score` column was calculated from the three subject scores.

## 5. Analysis performed

- Calculated the average, minimum, and maximum score for each subject.
- Calculated the average score for each student.
- Compared average scores by gender.
- Compared students who completed test preparation with those who did not.
- Displayed the five students with the highest average scores.

## 6. Results

Run the notebook and copy the values from `results/score_summary.csv` into the table below.

| Measure | Math | Reading | Writing | Overall average |
|---|---:|---:|---:|---:|
| Average | — | — | — | — |
| Minimum | — | — | — | — |
| Maximum | — | — | — | — |

## 7. Findings

Complete these statements using the generated result tables:

1. The subject with the highest average score was __________.
2. The highest individual average score was __________.
3. Students who completed test preparation had an average score of __________.
4. Students who did not complete test preparation had an average score of __________.
5. One important pattern observed in the data was __________.

## 8. Conclusion

This project demonstrated how Pandas and NumPy can be used to clean, summarize, and analyze a real CSV dataset. The analysis produced clear statistics about student performance and created reusable output files for reporting.

## 9. Dataset source

Students Performance in Exams, Kaggle:  
https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
