#!/usr/bin/env python3

'''
Q1.py
  Author(s): Bassem Sourour, Wasayuddin Syed, Shayan Safaei, Oliver Simm

  Question 1: How does the level of education affect the duration of job vacancies in a Canadian industry from 2022 to 2023?

 Parameters: Province, Education Level
 Fields: Year, Province, Education, Duration of job vacancy
 Files: CSV file of the entire table based on data source
 
 How Fields Affect Question: The fields listed above are important to the question because those are the main fields we look at when answering the question of how the level of education affects the duration of job vacancies. The level of education and duration of job vacancies are the important fields because that is what we use to see how long the duration of job vacancies is depending on education level. Provinces are also a very important field when looking into different education levels and duration of job vacancy statistics.


     Commandline Parameters: 5
        argv[0] = name of python file
        argv[1] = education level csv file
        argv[2] = duration of job vacancies csv file
        argv[3] = geo name
        argv[4] = education level

     Data Sources: 
        Archived - Job vacancies, proportion of job vacancies and average offered hourly wage by occupation and minimum level of education sought, quarterly, unadjusted for seasonality, inactive
        https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032805 


        Archived - Job vacancies, proportion of job vacancies and average offered hourly wage by occupation and duration of job vacancy, quarterly, unadjusted for seasonality, inactive
        https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032803 


'''
#imports
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv

from PIL.EpsImagePlugin import field



def main(argv):

    # Check that we have been given the right number of parameters
    if len(argv) != 5:
        print("Usage: Q1.py Q1data_education.csv Q1data_duration.csv <province> <education level>")
        sys.exit(1)

    # Command line arguments
    csv_education = argv[1]
    csv_duration = argv[2]
    geo_name = argv[3]
    education = argv[4]
    
    # Naming the new csv file
    new_csv = "preprocessed_q1.csv"

    # Storing the years needed
    yearRange = ["2022-01","2022-04","2022-07","2022-10","2023-01","2023-04",
                "2023-07"]
                
    # Opening both the csv files
    try:
        education_csv = open(csv_education, encoding="utf-8-sig")
    except IOError as err:
        print("Unable to open names file '{}' : {}".format(
                    csv_education, err), file=sys.stderr)
        sys.exit(1)
        
    try:
        duration_csv = open(csv_duration, encoding="utf-8-sig")
    except IOError as err:
        print("Unable to open names file '{}' : {}".format(
                    csv_duration, err), file=sys.stderr)
        sys.exit(1)

    education_reader = csv.reader(education_csv)
    duration_reader = csv.reader(duration_csv)
    
   # Validation flags
    province_found = False
    education_found = False

    # Open the file once and validate while iterating
    education_csv.seek(0)  # Going to the beginning of the csv file
    for row_data in education_reader:
        if "GEO" in row_data and "Job vacancy characteristics" in row_data:
            geo_index = row_data.index("GEO")
            jv_index = row_data.index("Job vacancy characteristics")
            continue  # Skip header row

        if len(row_data) > max(geo_index, jv_index):
            if row_data[geo_index] == geo_name:
                province_found = True
            if row_data[jv_index] == education:
                education_found = True

        # If both are found early, exit the loop
        if province_found == True and education_found == True:
            break

    # Check validation results
    if province_found == False:
        print(f"Error: '{geo_name}' is not a valid province.")
        sys.exit(1)

    if education_found == False:
        print(f"Error: '{education}' is not a valid education level.")
        sys.exit(1)


    # Closing file
    education_csv.close()
    
    # Reopening the file to start from the beginning
    try:
        education_csv = open(csv_education, encoding="utf-8-sig")
    except IOError as err:
        print("Unable to open names file '{}' : {}".format(
                    csv_education, err), file=sys.stderr)
        sys.exit(1)
        
    education_reader = csv.reader(education_csv)
        

    # Create new csv file
    try:
        with open(new_csv, 'w', newline='', encoding='utf-8') as output_csv:
            # Create CSV writer
            csv_writer = csv.writer(output_csv)
            
            # Write header
            csv_writer.writerow(["REF_DATE", "GEO", "National Occupational Classification",
                                "Job vacancy characteristics", "Statistics", "VALUE"])

            # We initialize these variables to zeros as we use them for counters below
            index_counter = 0
            index_counter2 = 0

            # For loop to get the index values of the header in the education csv file
            for row_data in education_reader:

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

            # For loop to get the index values of the header in the duration csv file
            for row_data2 in duration_reader:

                for col_data2 in row_data2:
                    if col_data2 == "REF_DATE":
                       ref_index2 = index_counter2
                    elif col_data2 == "GEO":
                        geo_index2 = index_counter2
                    elif col_data2 == "National Occupational Classification":
                        NOC_index2 = index_counter2
                    elif col_data2 == "Job vacancy characteristics":
                        jv_index2 = index_counter2
                    elif col_data2 == "Statistics":
                        stats_index2 = index_counter2
                    elif col_data2 == "VALUE":
                        val_index2 = index_counter2
                    index_counter2 +=1
                break

            
            
            print("REF_DATE,GEO,National Occupational Classification,Job vacancy characteristics,Statistics,VALUE")
            # For loop to get the right rows to get the assoicated data in the education csv file
            for row_data_field in education_reader:
                if row_data_field[ref_index] in yearRange:
                    if row_data_field[geo_index] == geo_name:
                        if row_data_field[NOC_index] == "Total, all occupations":
                            if row_data_field[jv_index] == education:
                                if row_data_field[stats_index] == "Job vacancies":
                                
                                    # Printing out the data and writing it in the new csv file
                                    if row_data_field[val_index] == "":
                                        print(f"{row_data_field[ref_index]},{row_data_field[geo_index]},{row_data_field[NOC_index]},{row_data_field[jv_index]},{row_data_field[stats_index]},0")
                                    else:
                                        csv_writer.writerow([
                                        row_data_field[ref_index],
                                        row_data_field[geo_index],
                                        row_data_field[NOC_index],
                                        row_data_field[jv_index],
                                        row_data_field[stats_index],
                                        row_data_field[val_index]])
                                        print(f"{row_data_field[ref_index]},{row_data_field[geo_index]},{row_data_field[NOC_index]},{row_data_field[jv_index]},{row_data_field[stats_index]},{row_data_field[val_index]}")

            # For loop to get the right rows to get the assoicated data in the duration csv file
            for row_data_field2 in duration_reader:
                if row_data_field2[ref_index2] in yearRange:
                    if row_data_field2[geo_index2] == geo_name:
                        if row_data_field2[NOC_index2] == "Total, all occupations":
                            if row_data_field2[jv_index2] in (
                                    "Less than 15 days",
                                    "15 to 29 days",
                                    "30 to 59 days",
                                    "60 to 89 days",
                                    "90 days or more",
                                ):
                                if row_data_field2[stats_index2] == "Job vacancies":
                                
                                    # Printing out the data and writing it in the new csv file
                                    if row_data_field2[val_index2] == "":
                                        print(f"{row_data_field2[ref_index2]},{row_data_field2[geo_index2]},{row_data_field2[NOC_index2]},{row_data_field2[jv_index2]},{row_data_field2[stats_index2]},0")
                                    else:
                                        csv_writer.writerow([
                                        row_data_field2[ref_index2],
                                        row_data_field2[geo_index2],
                                        row_data_field2[NOC_index2],
                                        row_data_field2[jv_index2],
                                        row_data_field2[stats_index2],
                                        row_data_field2[val_index2]])
                                        print(f"{row_data_field2[ref_index2]},{row_data_field2[geo_index2]},{row_data_field2[NOC_index2]},{row_data_field2[jv_index2]},{row_data_field2[stats_index2]},{row_data_field2[val_index2]}")
                                    
    except IOError as err:
        print(f"Error writing to output file '{new_csv}' : {err}", file=sys.stderr)
        sys.exit(1)

    # Close input files
    education_csv.close()
    duration_csv.close()
    
    #
    #   End of Function
    #

##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)


#
#   End of Script
#
