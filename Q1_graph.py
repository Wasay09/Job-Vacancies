#!/usr/bin/env python3

'''
Q1_graph.py
  Author(s): Bassem Sourour, Wasayuddin Syed, Shayan Safaei, Oliver Simm

  Question 1: How does the level of education affect the duration of job vacancies in a Canadian industry from 2022 to 2023?

 Parameters: Province, Education Level
 Fields: Year, Province, Education, Duration of job vacancy
 Files: CSV file of the entire table based on data source
 
 How Fields Affect Question: The fields listed above are important to the question because those are the main fields we look at when answering the question of how the level of education affects the duration of job vacancies. The level of education and duration of job vacancies are the important fields because that is what we use to see how long the duration of job vacancies is depending on education level. Provinces are also a very important field when looking into different education levels and duration of job vacancy statistics.


     Commandline Parameters: 2
        argv[0] = name of python file
        argv[1] = preprocessed data csv file

     Data Sources: 
        Archived - Job vacancies, proportion of job vacancies and average offered hourly wage by occupation and minimum level of education sought, quarterly, unadjusted for seasonality, inactive
        https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032805 


        Archived - Job vacancies, proportion of job vacancies and average offered hourly wage by occupation and duration of job vacancy, quarterly, unadjusted for seasonality, inactive
        https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032803 


'''
import pandas as pd
import matplotlib.pyplot as plt
import sys

YEAR_RANGE = [
    "2022-01", "2022-04", "2022-07",
    "2022-10", "2023-01", "2023-04", "2023-07"
]

def create_vacancy_data(filtered_df):
    education_vacancies = {}

    # Collect job vacancies for each education level
    education_levels = filtered_df["Job vacancy characteristics"].unique()

    for education in education_levels:
        vacancies = []
        for year in YEAR_RANGE:
            match = filtered_df[
                (filtered_df["REF_DATE"] == year) &
                (filtered_df["Job vacancy characteristics"] == education)
            ]
            
            if not match.empty:
                vacancies.append(match["VALUE"].iloc[0])
            else:
                vacancies.append(0)
        
        education_vacancies[education] = vacancies

    return education_vacancies

def plot_education_vacancies(education_vacancies):
    # Create subplots for each education level side by side (horizontally)
    num_plots = len(education_vacancies)
    fig, axes = plt.subplots(1, num_plots, figsize=(6 * num_plots, 6))

    if num_plots == 1:  # Handle the case with only one education level
        axes = [axes]

    # Loop through each education level and plot a graph
    for i, (education, vacancies) in enumerate(education_vacancies.items()):
        axes[i].plot(YEAR_RANGE, vacancies, marker='o', label=education, color='b')
        axes[i].set_title(f"{education}")
        axes[i].set_xlabel("Year")
        axes[i].set_ylabel("Job Vacancies")
        axes[i].legend()
        axes[i].grid(True, linestyle='--', alpha=0.7)

    # Adjust layout to prevent overlap
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

    education_vacancies = create_vacancy_data(filtered_df)
    plot_education_vacancies(education_vacancies)

if __name__ == "__main__":
    main(sys.argv)
