#code to add to main file

""""
def median(number_list):
    sorted_list = sorted(number_list)
    length = len(number_list)
    index = (length - 1)

    if(length % 2):
        result = sorted_list[index]
    else:
        result = (sorted_list[index] + sorted_list[index + 1]) / 2.0

    return result

def main():
    numbers = [4, 5, 8, 9, 10, 17]
"""
import csv

# this function uses the csv library to load each column into a list
def load_lists(filename):
    open_file = open(filename, 'r')

    file = csv.DictReader(open_file)

    month = []
    day = []
    dep_del15 = []
    dep_time_blk = []
    distance_group = []
    segment_number = []
    concurrent_flights = []
    number_of_seats = []
    carrier_name = []
    airport_flights_month = []
    airline_flights_month = []
    airline_airport_flights_month = []
    avg_monthly_pass_airport = []
    avg_monthly_pass_airline = []
    flt_attendants_per_pass = []
    ground_serv_per_pass = []
    plane_age = []
    departing_airport = []
    latitude = []
    longitude = []
    previous_airport = []
    prcp = []
    snow = []
    snwd = []
    tmax = []
    awnd = []
    carrier_hist = []
    dep_airport_hist = []
    day_hist = []
    dep_block_hist = []


    for col in file:
        month.append(col['MONTH'])
        day.append(col['DAY_OF_WEEK'])
        dep_del15.append(col['DEP_DEL15'])
        dep_time_blk.append(col['DEP_TIME_BLK'])
        distance_group.append(col['DISTANCE_GROUP'])
        segment_number.append(col['SEGMENT_NUMBER'])
        concurrent_flights.append(col['CONCURRENT_FLIGHTS'])
        number_of_seats.append(col['NUMBER_OF_SEATS'])
        carrier_name.append(col['CARRIER_NAME'])
        airport_flights_month.append(col['AIRPORT_FLIGHTS_MONTH'])
        airline_flights_month.append(col['AIRLINE_FLIGHTS_MONTH'])
        airline_airport_flights_month.append(col['AIRLINE_AIRPORT_FLIGHTS_MONTH'])
        avg_monthly_pass_airport.append(col['AVG_MONTHLY_PASS_AIRPORT'])
        avg_monthly_pass_airline.append(col['AVG_MONTHLY_PASS_AIRLINE'])
        flt_attendants_per_pass.append(col['FLT_ATTENDANTS_PER_PASS'])
        ground_serv_per_pass.append(col['GROUND_SERV_PER_PASS'])
        plane_age.append(col['PLANE_AGE'])
        departing_airport.append(col['DEPARTING_AIRPORT'])
        latitude.append(col['LATITUDE'])
        longitude.append(col['LONGITUDE'])
        previous_airport.append(col['PREVIOUS_AIRPORT'])
        prcp.append(col['PRCP'])
        snow.append(col['SNOW'])
        snwd.append(col['SNWD'])
        tmax.append(col['TMAX'])
        awnd.append(col['AWND'])
        carrier_hist.append(col['CARRIER_HISTORICAL'])
        dep_airport_hist.append(col['DEP_AIRPORT_HIST'])
        day_hist.append(col['DAY_HISTORICAL'])
        dep_block_hist.append(col['DEP_BLOCK_HIST'])
    
    print(month)


# this function loads the original file into a list, removes rows with 'NONE',
# then writes the list into a new file.
def remove_missing(filename):
    lines = []
    missing = 'NONE'

    with open(filename, 'r') as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == missing:
                    lines.remove(row)
    with open('No_Missing_Values.csv', 'w', newline='') as write_file:
        writer = csv.writer(write_file)
        writer.writerows(lines)

# this function takes the column and the value of the user's choosing,
# and returns the amount of times that value's in the column.
def count_distinct_value(column, value):
    count = 0
    for i in column:
        if i == value:
            count += 1

    return count
    

remove_missing('Airline_Delays_500_Lines.csv')
load_lists('No_Missing_Values.csv')

