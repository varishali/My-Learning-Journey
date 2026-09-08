#  Smart Automated Assignment Plagiarism Checker

An automated Python tool designed to detect similarity across multiple code/text submissions, calculate plagiarism percentages using `difflib.SequenceMatcher`, apply 5-level threshold classification, and display/export clean reports via Pandas.

---

## ✨ Features

- **Automated Directory Scanning:** Scans all `.py` and `.txt` files inside the designated `submissions/` directory.
- **Code Normalization:** Cleans comments, docstrings, and extra whitespaces before comparison.
- **5-Level Plagiarism Threshold:**
  -  `EXACT MATCH (100%)`
  -  `HIGH PLAGIARISM` (>= 75%)
  -  `MODERATE MATCH` (>= 50%)
  -  `LOW MATCH` (>= 25%)
  -  `SAFE / UNIQUE` (< 25%)
- **Visual Output:** Colored terminal headers using `colorama`.
- **Data Presentation:** Formatted DataFrame table output and automatic export to `plagiarism_report.csv`.

---

## 🛠️ Requirements

Install necessary packages using `pip`:

```bash
pip install colorama pandas