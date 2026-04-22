# Canadian Job Vacancy Analysis

A Python-based data analysis tool that explores Canadian job vacancy trends using Statistics Canada datasets. Built as a group project for CIS*2250 (Software Systems Development and Integration) at the University of Guelph.

---

## Overview

This project investigates three research questions about Canadian job vacancies using open data from Statistics Canada. Each question has its own preprocessing pipeline and visualization, all accessible through a shared interactive menu.

**Question 1 — Education & Vacancy Duration:**  
How does the level of education affect the duration of job vacancies across Canadian provinces (2022–2023)?

**Question 2 — COVID-19 & Full-time vs Part-time Vacancies:**  
How did COVID-19 affect the number of full-time and part-time job vacancies per province (Q4 2019 – Q2 2023)?

**Question 3 — Experience Level & Occupation:**  
How are job vacancies affected by experience level across different occupations (2022–2023)?

---

## Requirements

- Python 3.x
- [matplotlib](https://matplotlib.org/)
- [numpy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)

Install dependencies:

```bash
pip install matplotlib numpy pandas
```

---

## Data Sources

All datasets come from Statistics Canada (archived, quarterly, unadjusted for seasonality):

| Question | Table | Link |
|----------|-------|------|
| Q1 (Education) | 14-10-0328-05 | [statcan.gc.ca](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032805) |
| Q1 (Duration) | 14-10-0328-03 | [statcan.gc.ca](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032803) |
| Q2 (Full/Part-time) | 14-10-0328-01 | [statcan.gc.ca](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032801) |
| Q3 (Experience) | 14-10-0328-07 | [statcan.gc.ca](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032807) |

To download: on each page, click **Download options** → select **"Download entire table"** (second-last option) to get the full CSV.

---

## Project Structure

```
Job-Vacancies/
├── main.py                 # Interactive menu — entry point for all questions
├── Q1.py                   # Q1 preprocessing (education + duration CSVs → preprocessed_q1.csv)
├── Q1_graph.py             # Q1 visualization (line graphs)
├── preprocessQ2.py         # Q2 preprocessing (14100328.csv → preprocessed_q2.csv)
├── DemoQ2.py               # Q2 visualization (full-time vs part-time line graph)
├── Q3Filter.py             # Q3 preprocessing (14100328.csv → preprocessed_q3.csv)
├── Q3Plot.py               # Q3 visualization (bar charts by occupation)
├── preprocessed_q1.csv     # Pre-generated Q1 data
├── preprocessed_q2.csv     # Pre-generated Q2 data
└── preprocessed_q3.csv     # Pre-generated Q3 data
```

---

## Usage

### Step 1 — Preprocess the data

Each question requires its own preprocessing step using the raw Statistics Canada CSVs.

**Q1:**
```bash
python3 Q1.py Q1data_education.csv Q1data_duration.csv "Province" "Education Level"
```

**Q2:**
```bash
python3 preprocessQ2.py 14100328.csv > preprocessed_q2.csv
```

**Q3:**
```bash
python3 Q3Filter.py 14100328.csv "Province" "Occupation 1" "Occupation 2"
```

> Pre-processed CSV files are included in the repo, so you can skip this step if you just want to run the visualizations.

### Step 2 — Run the main program

```bash
python3 main.py preprocessed_q1.csv preprocessed_q2.csv preprocessed_q3.csv
```

You will be presented with an interactive menu:

```
Enter a choice (1.Run Q1    2.Run Q2    3.Run Q3    -1: Exit):
```

Select a question number and follow the prompts to enter your parameters.

---

## Valid Parameters

### Provinces (all questions)

Canada, Alberta, British Columbia, Manitoba, New Brunswick, Newfoundland and Labrador, Nova Scotia, Ontario, Prince Edward Island, Quebec, Saskatchewan, Nunavut, Northwest Territories, Yukon

### Education Levels (Q1)

- Minimum level of education required, all levels
- No minimum level of education required
- High school diploma or equivalent
- Non-university certificate or diploma
- University certificate or diploma below bachelor's level
- Bachelor's degree
- University certificate, diploma or degree above the bachelor's level

### Occupations (Q3)

- Management occupations [0]
- Business, finance and administration occupations [1]
- Natural and applied sciences and related occupations [2]
- Health occupations [3]
- Occupations in education, law and social, community and government services [4]
- Occupations in art, culture, recreation and sport [5]
- Sales and service occupations [6]
- Trades, transport and equipment operators and related occupations [7]
- Natural resources, agriculture and related production occupations [8]
- Occupations in manufacturing and utilities [9]

> **Note:** Parameter values are case-sensitive and must match the exact spelling and spacing shown above.

---
### Contributors
Wasayuddin Syed, Oliver Simm, Bassem Sourour, Shayan Safaei


## License

This project uses open data from [Statistics Canada](https://www.statcan.gc.ca/). All datasets are subject to the Statistics Canada Open Licence.
