"""
    Cis2250DemoQ3.py
    Author(s):Shayan Safaei, Oliver Simm, Bassem Sourour, Wasayuddin Syed


Question 3: How is job vacancy affected throughout 2022 to 2023 in a specific job industry?


Parameters: Province, Occupation(s)
Fields:  Years (Q1 2022 -> Q4 2023), Job vacancy characteristics, Job vacancies (Value), Reference Date, Geographical Status, National Occupational Classification
Files: CSV file of entire table based on data source


How Fields Affect Question: Based on user choice, they will be given a set of information that they can then see how the chosen occupation is affected by change in year (Quarterly). This will let us see how much the difference in Job Vacancies is affected due to time in specific job industries.


Data Sources: Archived - Job vacancies, proportion of job vacancies and average offered hourly wage by occupation and minimum experience level sought, quarterly, unadjusted for seasonality, inactive 
https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032807


How to run syntax: | python script.py <input.csv> |


"""

import pandas as pd
import matplotlib.pyplot as plt
import sys

YEAR_RANGE = [
    "2022-01", "2022-04", "2022-07", 
    "2022-10", "2023-01", "2023-04", "2023-07"
]

def create_vacancy_data(filtered_df):
    occupations = filtered_df["National Occupational Classification"].unique()
    vacancy_data = {}

    for occupation in occupations:
        values = []
        for year in YEAR_RANGE:
            match = filtered_df[
                (filtered_df["REF_DATE"] == year) &
                (filtered_df["National Occupational Classification"] == occupation)
            ]

            if not match.empty:
                values.append(match["VALUE"].iloc[0])
            else:
                values.append(0)

        vacancy_data[occupation] = values

    return vacancy_data

def plot_bar_chart(vacancy_data):
    fig, axes = plt.subplots(1, len(vacancy_data), figsize=(18, 5))

    if len(vacancy_data) == 1:
        axes = [axes]

    for i, (occupation, values) in enumerate(vacancy_data.items()):
        axes[i].bar(YEAR_RANGE, values, color="skyblue")
        axes[i].set_title(occupation, wrap=True)
        axes[i].set_xlabel("Years (Quarterly)")
        axes[i].set_ylabel("Job Vacancies")
        axes[i].tick_params(axis='x', rotation=45)

    plt.tight_layout(pad=3.0)
    plt.show()

def main(argv):
    if len(argv) != 2:
        print("Usage: python plot_from_filtered.py <filtered_csv>")
        sys.exit(1)

    filtered_csv = argv[1]

    try:
        filtered_df = pd.read_csv(filtered_csv)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)

    vacancy_data = create_vacancy_data(filtered_df)
    plot_bar_chart(vacancy_data)

if __name__ == "__main__":
    main(sys.argv)
