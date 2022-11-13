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

class Airline:
    
    column_names = []
    num_of_columns = []
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


    # this function loads the original file into a list, removes rows with 'NONE',
    # then writes the list into a new file.
    def __init__(self, filename):
        lines = []
        missing = 'NONE'

        with open(filename, 'r') as read_file:
            reader = csv.reader(read_file)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == missing:
                        lines.remove(row)

        # for loop to ensure no duplicates are added
        no_dup = []
        for i in lines:
            if i not in no_dup:
                no_dup.append(i)

        with open('No_Missing_Values.csv', 'w', newline='') as write_file:
            writer = csv.writer(write_file)
            writer.writerows(no_dup)

        self.load_lists('No_Missing_Values.csv')

    # this function uses the csv library to load each column into a list
    def load_lists(self, filename):
        with open(filename) as csv_file:
            reader = csv.reader(csv_file)
            self.column_names = next(reader)

        self.num_of_columns = len(self.column_names)

        open_file = open(filename, 'r')

        file = csv.DictReader(open_file)

        for col in file:
            self.month.append(col['MONTH'])
            self.day.append(col['DAY_OF_WEEK'])
            self.dep_del15.append(col['DEP_DEL15'])
            self.dep_time_blk.append(col['DEP_TIME_BLK'])
            self.distance_group.append(col['DISTANCE_GROUP'])
            self.segment_number.append(col['SEGMENT_NUMBER'])
            self.concurrent_flights.append(col['CONCURRENT_FLIGHTS'])
            self.number_of_seats.append(col['NUMBER_OF_SEATS'])
            self.carrier_name.append(col['CARRIER_NAME'])
            self.airport_flights_month.append(col['AIRPORT_FLIGHTS_MONTH'])
            self.airline_flights_month.append(col['AIRLINE_FLIGHTS_MONTH'])
            self.airline_airport_flights_month.append(col['AIRLINE_AIRPORT_FLIGHTS_MONTH'])
            self.avg_monthly_pass_airport.append(col['AVG_MONTHLY_PASS_AIRPORT'])
            self.avg_monthly_pass_airline.append(col['AVG_MONTHLY_PASS_AIRLINE'])
            self.flt_attendants_per_pass.append(col['FLT_ATTENDANTS_PER_PASS'])
            self.ground_serv_per_pass.append(col['GROUND_SERV_PER_PASS'])
            self.plane_age.append(col['PLANE_AGE'])
            self.departing_airport.append(col['DEPARTING_AIRPORT'])
            self.latitude.append(col['LATITUDE'])
            self.longitude.append(col['LONGITUDE'])
            self.previous_airport.append(col['PREVIOUS_AIRPORT'])
            self.prcp.append(col['PRCP'])
            self.snow.append(col['SNOW'])
            self.snwd.append(col['SNWD'])
            self.tmax.append(col['TMAX'])
            self.awnd.append(col['AWND'])
            self.carrier_hist.append(col['CARRIER_HISTORICAL'])
            self.dep_airport_hist.append(col['DEP_AIRPORT_HIST'])
            self.day_hist.append(col['DAY_HISTORICAL'])
            self.dep_block_hist.append(col['DEP_BLOCK_HIST'])
        
        #print(self.day)

    def drop_column(self, column):
        result = []
        if column == self.column_names[0]:
            self.column_names.remove(self.column_names[0])
            self.month.clear()
        if column == self.column_names[1]:
            self.column_names.remove(self.column_names[1])
            self.day.clear()
        """
        if num == 3:
            result = self.dep_del15
        if num == 4:
            result = self.dep_time_blk
        if num == 5:
            result = self.distance_group
        if num == 6:
            result = self.segment_number
        if num == 7:
            result = concurrent_flights
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
       """

    # this function takes the column and the value of the user's choosing,
    # and returns the amount of times that value's in the column.
    def count_distinct_value(column, value):
        count = 0
        for i in column:
            if i == value:
                count += 1

        return count

data = Airline('Airline_Delays_500_Lines.csv')

active = True

while(active):
    i = 0
    valid = False
    num = 1
    for value in data.column_names:
        print(num, ' - ', data.column_names[num-1])
        num += 1

    ans = input('Would you like to drop any columns? (y/n) ')
    if ans == 'y' or input == 'Y' or input == 'Yes':
        while(valid == False):
            ans = input('Enter the name of the column you\'d like to drop: ')
            for value in data.column_names:
                if ans == data.column_names[i]:
                    valid = True
                    break
                i += 1

            if(valid == False):
                print('Name given isn\'t valid, please try again')
            else:
                drop = data.drop_column(ans)
    
    num = 1
    for value in data.column_names:
        print(num, ' - ', data.column_names[num-1])
        num += 1


    active = False

