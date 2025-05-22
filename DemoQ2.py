"""
    Cis2250DemoQ2.py
    Author(s): Oliver Simm, Bassem Sourour, Wasayuddin Syed, Shayan Safaei


Question 2: How did the impact of COVID-19 affect the number of Full-time and Part-time job vacancies in all industries within a province or Canada from Q4 2019 to Q2 2023?


Parameters: Province
Fields:  Years (Q4 2019 -> Q2 2023), Statistics, Job vacancy characteristics, full-time: Job vacancies, part-time: job vacancies.
Files: CSV file of entire table based on data source


How Fields Affect Question: The year range from Q4 2019 to Q2 2023 allows for an analysis of pre- to post-pandemic levels of job vacancy data, the JVC are used to get the part-time and full-time data, and statistics are used to get the number of job vacancies for both part and full-time.


Data Sources: Archived - Job vacancies, proportion of job vacancies and average offered hourly wage by selected characteristics, quarterly, unadjusted for seasonality, inactive
https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032801&pickMembers%5B0%5D=1.1&pickMembers%5B1%5D=2.1&cubeTimeFrame.startMonth=01&cubeTimeFrame.startYear=2019&cubeTimeFrame.endMonth=10&cubeTimeFrame.endYear=2023&referencePeriods=20190101%2C20231001



"""
#imports
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv

from PIL.EpsImagePlugin import field


#define main function
def main(argv):

    #check if number of command line arguments are correct
    if len(argv) != 3:
        print("Usage: read_file.py <file name>")
        sys.exit(1)

    # command line arguments
    csv_filename = argv[1]
    geo_name = argv[2]
    

    #variables
    #quarts have 01,04,07,10 suffixes
    yearRange = ["2019-10","2020-01","2020-10","2021-01","2021-04","2021-07","2021-10","2022-01","2022-04","2022-07","2022-10","2023-01","2023-04"]

    #yearRange = ["2019-10","2020-01","2020-04","2020-07","2020-10","2021-01","2021-04","2021-07","2021-10","2022-01","2022-04","2022-07","2022-10","2023-01","2023-04"]
    #data 2020-04 and 07 not in data set
    #create lists to put values into
    partTimeValues = []
    fullTimeValues = []


    #Open the file
    try:
        csv_fh = open(csv_filename, encoding="utf-8-sig")

    except IOError as err:
        # Here we are using the python format() function.
        # The arguments passed to format() are placed into
        # the string it is called on in the order in which
        # they are given.
        print("Unable to open names file '{}' : {}".format(
                csv_filename, err), file=sys.stderr)
        sys.exit(1)
    
    #read the file
    csv_reader = csv.reader(csv_fh)


    # We initialize these variables to zeros as we use them for
    # counters below
    index_counter = 0

    # for loop to get the index values of the header
    for row_data in csv_reader:
        for col_data in row_data:
            if col_data == "REF_DATE":
               ref_index = index_counter
            elif col_data == "GEO":
                geo_index = index_counter
            elif col_data == "National Occupational Classification":
                NOC_index = index_counter
            elif col_data == "Job vacancy characteristics":
                jv_index = index_counter
            elif col_data == "Statistics":
                stats_index = index_counter
            elif col_data == "VALUE":
                val_index = index_counter
            index_counter +=1 
        break
    

    # Print required header
    print("REF_DATE,GEO,National Occupational Classification,Job vacancy characteristics,Statistics,VALUE")
    
    for row_data_field in csv_reader:
        #print(f"Geo: {row_data_field[geo_index]}, NOC: {row_data_field[NOC_index]}")
        if row_data_field[ref_index] in yearRange:
            if row_data_field[geo_index] == geo_name:
                if row_data_field[NOC_index] == "Total, all occupations":
                    if row_data_field[jv_index] == "Full-time" or row_data_field[jv_index] == "Part-time":
                        if row_data_field[stats_index] == "Job vacancies":
                            #append values of part and full-time into repective lists
                            if row_data_field[jv_index] == "Full-time":
                                fullTimeValues.append(row_data_field[val_index])
                            if row_data_field[jv_index] == "Part-time":
                                partTimeValues.append(row_data_field[val_index])
                            if row_data_field[val_index] == "":
                                print(f"{row_data_field[ref_index]},{row_data_field[geo_index]},{row_data_field[NOC_index]},{row_data_field[jv_index]},{row_data_field[stats_index]},0")
                            else:
                                print(f"{row_data_field[ref_index]},{row_data_field[geo_index]},{row_data_field[NOC_index]},{row_data_field[jv_index]},{row_data_field[stats_index]},{row_data_field[val_index]}")

    #print full and part-time lists
    print("Full: ",fullTimeValues)
    print("Part: ",partTimeValues)

    #convert full and part-time value lists into numpy arrays with a float cast
    fullTimeValues = np.array(fullTimeValues, dtype=float)  # Ensure numerical type
    partTimeValues = np.array(partTimeValues, dtype=float)  # Ensure numerical type

    plt.figure(figsize=(12, 6)) # size of graph

    #plot full and part-time vacancy on the graph
    plt.plot(yearRange, fullTimeValues, marker='o', linestyle='-', color='b',label="Full-time Job Vacancies")
    plt.plot(yearRange, partTimeValues, marker='s', linestyle='--', color='orange',label="Part-time Job Vacancies")


    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Number of Job Vacancies")
    plt.title(f"Full-time and Part-time Job Vacancies in {geo_name} (2019-2023)")
    plt.legend()  # Show legend for both Full and Part time vacancies
    plt.grid(True) #enable grid

    plt.show() # show graph



    #-----------Close file

#call main function
main(sys.argv)