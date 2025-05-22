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


How to run syntax: | python script.py <input_csv> <geo> <occupation_1> [<occupation_2> ...] |


"""


import pandas as pd
import sys

YEAR_RANGE = [
    "2022-01", "2022-04", "2022-07", 
    "2022-10", "2023-01", "2023-04", "2023-07"
]

def preprocess_csv(input_csv, geo, occupations):
    try:
        df = pd.read_csv(input_csv, usecols=[
            "REF_DATE", 
            "GEO", 
            "National Occupational Classification", 
            "Job vacancy characteristics", 
            "VALUE"
        ])
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)


    filtered_df = df[
        (df["GEO"] == geo) &
        (df["REF_DATE"].isin(YEAR_RANGE)) &
        (df["Job vacancy characteristics"] == "Minimum experience level sought, all levels") & #Used to get all job vacanciess
        (df["National Occupational Classification"].isin(occupations))
    ]

    filtered_df = filtered_df.sort_values(by=[
        "National Occupational Classification", "REF_DATE"
    ])

    return filtered_df

def main(argv):
    if len(argv) < 4:
        print("Usage: python script.py <input_csv> <geo> <occupation_1> [<occupation_2> ...]")
        sys.exit(1)

    input_csv = argv[1]
    geo = argv[2]
    occupations = argv[3:]


    output_csv = "preprocessed_q3.csv"

    filtered_df = preprocess_csv(input_csv, geo, occupations)

    if filtered_df.empty:
        print("No data found for the given province and occupations. Please check your input.")
        sys.exit(1)

    try:
        filtered_df.to_csv(output_csv, index=False)
        print(f"Filtered data saved to: {output_csv}")
    except Exception as e:
        print(f"Error saving output CSV: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv)