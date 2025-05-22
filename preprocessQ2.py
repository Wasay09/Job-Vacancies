import sys
import csv




def main(argv):

    # command line arguments
    csv_filename = argv[1]
    geo_name = ["Canada","Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Nova Scotia", "Ontario", "Prince Edward Island", "Quebec","Saskatchewan","Nunavut", "Northwest Territories","Yukon"]
    yearRange = ["2019-10","2020-01","2020-10","2021-01","2021-04","2021-07","2021-10","2022-01","2022-04","2022-07","2022-10","2023-01","2023-04"]

    # Open the file
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

    # read the file
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
            index_counter += 1
        break

    #put into csv
    print("\"REF_DATE\",\"GEO\",\"National Occupational Classification\",\"Job vacancy characteristics\",\"Statistics\",\"VALUE\"")

    #if the data matches our output then enter it into the file
    for row_data_field in csv_reader:
        # print(f"Geo: {row_data_field[geo_index]}, NOC: {row_data_field[NOC_index]}")
        if row_data_field[ref_index] in yearRange:
            if row_data_field[geo_index] in geo_name:
                if row_data_field[NOC_index] == "Total, all occupations":
                    if row_data_field[jv_index] == "Full-time" or row_data_field[jv_index] == "Part-time":
                        if row_data_field[stats_index] == "Job vacancies":
                            print(f"\"{row_data_field[ref_index]}\",\"{row_data_field[geo_index]}\",\"{row_data_field[NOC_index]}\",\"{row_data_field[jv_index]}\",\"{row_data_field[stats_index]}\",\"{row_data_field[val_index]}\"")



main(sys.argv)


