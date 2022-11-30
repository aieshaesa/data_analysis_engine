#####################################################################
# CRSE: CMPS3500
# ASGT: Class Project
# Python Implementation: Basic Data Analysis
# DATE: 11/05/2022
# Student 1: Aiesha Esa
# Student 2: Mostafa Abadi
# Student 3: Spencer Denney
# Student 4: Hector Martinez
# DESCRIPTION: Implementation Basic Data Analysis Routines
#####################################################################

# code to add to main file
# 11/21/2022

import csv
import math

# color formatting for terminal
MAKE_RED = "\u001b[31;1m"
MAKE_BLUE = "\u001b[34;1m"
MAKE_GREEN = "\u001b[32;1m"
MAKE_YELLOW = "\u001b[33;1m"
MAKE_MAGENTA = "\u001b[35;1m"
MAKE_CYAN = "\u001b[36;1m"
RESET = "\u001b[0m"



#open csv file
class Airport:
    columns_as_lists = []
    column = []
    size = 0

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

    def load_lists(self, file):
        with open(file) as csv_file:
            # creating an object of csv reader
            # with the delimiter
            csv_reader = csv.reader(csv_file, delimiter = ',')
        
            # loop to iterate through the rows of csv
            for row in csv_reader:
        
                # adding first row
                self.column.append(row)
        
                # breaking the loop after the
                # first iteration itself
                break

        csv_file.close()

        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            
            # number of columns
            self.size = int(len(self.column[0]))
            reader = csv.reader(csv_file)
            # stores each column into array
            self.columns_as_lists = [list(c) for c in zip(*reader)]
                
        self.remove_punctuation()

    # prints the menu to the terminal that servers as the main interface to the user.
    # all the options listed are the ones that are valid to choose from.
    # not all actions can be made towards particular columns, so exceptions must be raised to prevent errors.
    def menu(self):
        valid = False
        options = ['Drop a Column', 'Count Distinct Value', 'Search for a Value', 'Sort a Column', 'Mean of a Column', 
            'Median of a Column', 'Mode of a Column', 'Standard Deviation', 'Variance', 'Minimum', 'Maximum',
            '20 Percentile', '40 Percentile', '50 Percentile', '60 Percentile', '80 Percentile', 'Print Rows', 'Analysis']

        options_length = len(options)

        for i in range(options_length):
            print(i+1, ':', options[i])

        while(valid == False):
            ans = int(input('What would you like to do? (1 - '+ str(options_length) +'): '))

            if ans < 1 or ans > options_length:
                print(MAKE_RED, 'Number given isn\'t valid, please try again', RESET)
            else:
                valid = True
        
        ans -= 1

        ##############################[ User Actions ]##############################

        column_number = None
        
        # if we are dropping columns, printing rows, or showing 
        # the analysis don't list the columns.
        if ans != 0 and ans != 16 and ans != 17:
            column_number = self.choose_column()
        
            chosen_column_list = self.list_for_chosen_column(column_number)
            chosen_column_header = self.columns_as_lists[column_number][0]
            
            chosen_column_length = len(chosen_column_list)

        try:
            if ans == 0:
                if self.size <= 1:
                    raise Exception("At least 1 column must remain in the dataset.")
                
                option = -1;
                self.print_column_names()

                while option < 1 or option > self.size:
                    option = int(input("Enter a column to drop (1 - "+ str(self.size) +"): "))

                column_dropped_header = self.columns_as_lists[option - 1][0]
                self.drop_column(option)

                print(MAKE_GREEN, 'Column', column_dropped_header, 'was dropped.', RESET)

            elif ans == 1:
                chosen_column_refined = self.list_for_chosen_column(column_number)
                unique_list = self.unique(chosen_column_refined)
                index = 0
                option = -1

                for value in unique_list:
                    index += 1
                    print(index, ":", value)
                
                while option < 1 or option > index:
                    option = int(input("Which value would you like to count? (1 - "+ str(index) +"): "))
                
                distinct_value, count = self.count_distinct_value(column_number, unique_list[option - 1])
                print(MAKE_GREEN, 'The amount of times', distinct_value, 'is in the data is', count, 'time(s).', RESET)

            elif ans == 2:
                user_input = -1

                while user_input < 1 or user_input > chosen_column_length:
                    user_input = int(input("Which row would you like to pick? (1 - "+ str(chosen_column_length) +"): "))

                chosen_column_refined = self.list_for_chosen_column(column_number)
                val = self.search_value(chosen_column_refined, user_input - 1)

                print(MAKE_GREEN, "The value at row", str(user_input), "of column", chosen_column_header, "is", str(val), RESET)

            elif ans == 3:
                self.sort_column(column_number)

            elif ans == 4:
                result_mean = self.mean(chosen_column_list)
                print(MAKE_GREEN, "The mean of the column", chosen_column_header, "is", result_mean, RESET)

            elif ans == 5:
                result_median = self.median(chosen_column_list)
                print(MAKE_GREEN, 'The median of the column', chosen_column_header, 'is:', result_median, RESET)

            elif ans == 6:
                result_mode = self.mode(chosen_column_list)
                print(MAKE_GREEN, 'The mode of the column', chosen_column_header, 'is:', result_mode, RESET)

            elif ans == 7:
                result_sd = self.standard_deviation(chosen_column_list)
                print(MAKE_GREEN, 'The standard deviation of the column', chosen_column_header, 'is:', result_sd, RESET)

            elif ans == 8:
                result_variance = self.variance(chosen_column_list)
                print(MAKE_GREEN, 'The variance of the column', chosen_column_header, 'is:', result_variance, RESET)

            elif ans == 9:
                result_min = self.minimum(chosen_column_list)
                print(MAKE_GREEN, "The minimum value of the column", chosen_column_header, "is", result_min, RESET)

            elif ans == 10:
                result_max = self.maximum(chosen_column_list)
                print(MAKE_GREEN, "The maximum value of the column", chosen_column_header, "is", result_max, RESET)

            elif ans == 11:
                result_per20 = self.percentile_20(chosen_column_list)
                print(MAKE_GREEN, "The 20th percentile value of the column", chosen_column_header, "is", result_per20, RESET)

            elif ans == 12:
                result_per40 = self.percentile_40(chosen_column_list)
                print(MAKE_GREEN, "The 40th percentile value of the column", chosen_column_header, "is", result_per40, RESET)

            elif ans == 13:
                result_per50 = self.percentile_50(chosen_column_list)
                print(MAKE_GREEN, "The 50th percentile value of the column", chosen_column_header, "is", result_per50, RESET)

            elif ans == 14:
                result_per60 = self.percentile_60(chosen_column_list)
                print(MAKE_GREEN, "The 60th percentile value of the column", chosen_column_header, "is", result_per60, RESET)

            elif ans == 15:
                result_per80 = self.percentile_80(chosen_column_list)
                print(MAKE_GREEN, "The 80th percentile value of the column", chosen_column_header, "is", result_per80, RESET)

            elif ans == 16:
                self.print_rows()

            elif ans == 17:
                self.print_analysis()

        except ValueError:
            print(MAKE_RED, 'The column you chose does not include integers or floats for this action.', RESET)

        except Exception as ex:
            print(MAKE_RED, ex, RESET)

        ############################################################################

    # prints each column in the dataset to the terminal.
    # this is needed to show options to the user which columns are available to work with.
    def print_column_names(self):
        for i in range(self.size):
            print(i+1,":", self.columns_as_lists[i][0])

        print("\n")

    # strips away quotes of a value in each column in the dataset.
    # each value in the dataset needs to be iterated over and be sanitized for
    # other processes to work purely with numbers or strings.
    def remove_punctuation(self):
        for i in range(len(self.columns_as_lists)):
            for j in range(len(self.columns_as_lists[i])):
                self.columns_as_lists[i][j] = self.columns_as_lists[i][j].replace('"', '')

    # determines if a column contains numerical numbers or not.
    # exception handing is needed because it needs to determine if an
    # item in the given generic list can be converted to a number or not.
    def column_is_numerical(self, values_list):
        if values_list[1].isdigit() or values_list[1].isnumeric():
            result = True

        # if it errors converting the string to number, then column isn't a numeric column.
        try:
            float(values_list[1])

            result = True
        except:
            result = False

        return result    
        
        
        
        
########################################## Fixed error with asc/desc printing #################################################
    # sorts a column given a choice of a column number.
    # checking if a column is numerical is needed to sort only numbers or only strings as keys.
    def sort_column(self, column_choice):
        column_chosen = self.columns_as_lists[column_choice]
        copy_of_column_chosen = column_chosen[1:]

        option = None

        while option != "asc" and option != "desc":
            option = input("Which sort order use? (asc|desc): ")

        if self.column_is_numerical(column_chosen):
            # ascending order
            if option == "asc":
                copy_of_column_chosen.sort(key = float)
                column_chosen[1:] = copy_of_column_chosen

                print(MAKE_GREEN, "Column " + str(column_chosen) + " sorted in ascending order.", RESET)

            # descending order
            elif option == "desc":
                copy_of_column_chosen.sort(reverse = True, key = float)
                column_chosen[1:] = copy_of_column_chosen

                print(MAKE_GREEN, "Column " + str(column_chosen) + " sorted in descending order.", RESET)
        else:
            # ascending order
            if option == "asc":
                copy_of_column_chosen.sort(key = str)
                column_chosen[1:] = copy_of_column_chosen

                print(MAKE_GREEN, "Column " + str(column_chosen) + " sorted in ascending order.", RESET)

            # descending order
            elif option == "desc":
                copy_of_column_chosen.sort(reverse = True, key = str)
                column_chosen[1:] = copy_of_column_chosen

                print(MAKE_GREEN, "Column " + str(column_chosen) + " sorted in descending order.", RESET)
###############################################################################################################





    # deletes a column from loaded dataset.
    # all the columns in the dataset are the only valid ones to be deleted,
    # and all other choices outside this range are invalid and disregarded.
    def drop_column(self, column_number):
        self.columns_as_lists.pop(column_number-1)
        self.size = len(self.columns_as_lists)

    # prints a menu to the user for available actions to the database.
    def choose_column(self):
        self.print_column_names()

        column_option = -1

        while(column_option < 1 or column_option > self.size):
            column_option = int(input('Enter the number of the column of you\'re choosing: '))

        return column_option - 1
    
    # converts a raw column set to either a list or a dictionary.
    # column headers are stripped away so indexing doesn't include the column header.
    # it convert a column into a numerically indexed list regardless if the given column is numerical or not.
    # returns: a list or dictionary of a given column.
    def list_for_chosen_column(self, column_number):
        raw_column = self.columns_as_lists[column_number]
        new_column = []

        if self.column_is_numerical(raw_column):
            for i in range(1, len(raw_column) - 1):
                new_column.append(float(raw_column[i]))
        else:
            new_column = {}

            for i in range(1, len(raw_column) - 1):   
                new_column[i - 1] = raw_column[i]

        return new_column
    
    # returns a value at a row in a generic list.
    def search_value(self, values_list, row):
        return values_list[row]

    # retrieves the number of occurences of a value in a given column.
    # it first checks if a column is numerical or not to make sure it's comparing
    # numbers to numbers and strings to strings.
    # returns: the value to look for, and the count as the result.
    def count_distinct_value(self, column_number, value_to_look):
        chosen_column_list = self.columns_as_lists[column_number][1:]
        count = 0

        if self.column_is_numerical(chosen_column_list):
            for value in chosen_column_list:
                if float(value) == float(value_to_look):
                    count += 1
        else:
            for value in chosen_column_list:
                if value == value_to_look:
                    count += 1

        return value_to_look, count

    # creates a list of unique values of a given generic list.
    # it will convert both dictionaries and sets into a list that can be indexed.
    # returns: a list of uniquely mapped values.
    def unique(self, values_list):
        converted_list = None

        if type(values_list) is dict:
            converted_list = list(values_list.values())
        else:
            converted_list = values_list
        
        return list(set(converted_list))
    
    # returns the mean of a generic list.
    def mean(self, values_list):
        if type(values_list) is not list:
            raise ValueError

        sum = 0
        mean = None

        for i in range(len(values_list)):
            sum = sum + values_list[i]

        mean = (sum / len(values_list))
        
        return mean
    
    # returns the median of a generic list.
    def median(self, values_list):
        if type(values_list) is not list:
            raise ValueError

        count = len(values_list)
        sorted_list = sorted(values_list)

        median = values_list[0]

        # get index of middle number.
        middleIndex = math.floor(count / 2)

        # scenario 1: if the count is odd, return the middle-most number.
        if (count % 2) == 1:
            median = sorted_list[middleIndex]

        # scenario 2: if the count is even, then get the mean of the two middle numbers.
        else: 
            lower_middle_num = sorted_list[middleIndex - 1]
            upper_middle_num = sorted_list[middleIndex]
            median = self.mean([lower_middle_num, upper_middle_num])

        return median

    # returns the mode of a generic list.
    def mode(self, values_list):
        if type(values_list) is not list:
            raise ValueError

        sorted_list = sorted(values_list)
        
        last_num = sorted_list[0]
        last_num_occurrences = 0
        current_num_occurrences = 0

        mode = sorted_list[0]

        for num in sorted_list:
            if last_num == num:
                # increment this number's occurence as long as we keep iterating over the same number
                current_num_occurrences += 1
            
            # if this number's occurrences passes the previous number's occurrences, make this number the new mode.
            if current_num_occurrences > last_num_occurrences:            
                mode = last_num
                last_num_occurrences = current_num_occurrences

            # if this current number we are reading isn't the same as the last number iterated, 
            # reset the occurrences value for this new number.
            if last_num != num:
                current_num_occurrences = 1
            
            # set the previous iterated item to this (current) one.
            last_num = num

        return mode

    # returns the standard deviation of a generic list.
    # the standard deviation is the square root of the variance, 
    # so variance function must be used for the calculation.
    def standard_deviation(self, values_list):
        if type(values_list) is not list:
            raise ValueError

        list_variance = self.variance(values_list)
        standard_deviation = math.sqrt(list_variance)

        return standard_deviation

    # returns the variance of a generic list.
    # each item in the list must be calculated in order to
    # calculate the variance overall.
    def variance(self, values_list):
        if type(values_list) is not list:
            raise ValueError

        variance = 0
        difference = 0

        list_mean = self.mean(values_list)
        
        for num in values_list:
            # for each number, substract it by the mean of the list, then square it, and add it to the difference.
            difference = difference + (num - list_mean) ** 2
        
        variance = difference / len(values_list)

        return variance

    # returns the minimum value contained in a given generic list.
    def minimum(self, values_list):
        if type(values_list) is not list:
            raise ValueError

        minimum = min(values_list)
        return minimum

    # returns the maximum value contained in a given generic list.
    def maximum(self, values_list):
        if type(values_list) is not list:
            raise ValueError

        maximum = min(values_list)
        return maximum

    ### percentile_20, percentile_40, percentile_50, percentile_60, percentile_80 ###
    # returns the value at the 20th, 40th, 60th and 80th percentile of a given generic list.
    def percentile_20(self, values_list):
        if type(values_list) is not list:
            raise ValueError

        count = len(values_list)
        sorted_list = sorted(values_list)
        
        rank = (0.20 * (count - 1)) + 1
        
        # if rank is an integer, then use the rank as an index and get the value at that index.
        if rank.is_integer():
            percentile = sorted_list[math.floor(rank) - 1]
        else:
            # if rank is a float, then get the value at that index as a integer, then add the rank's 
            # part to its whole part, as the percentile. 
            # We thought we had to return the actual value in the array, instead of a float, so we return that as well.
            percentile = sorted_list[math.floor(rank) - 1]
        
        return percentile

    def percentile_40(self, values_list):
        if type(values_list) is not list:
            raise ValueError

        count = len(values_list)
        sorted_list = sorted(values_list)
        
        rank = (0.40 * (count - 1)) + 1
        
        if rank.is_integer():
            percentile = sorted_list[math.floor(rank) - 1]
        else:
            percentile = sorted_list[math.floor(rank) - 1]
        
        return percentile

    def percentile_50(self, values_list):
        if type(values_list) is not list:
            raise ValueError

        count = len(values_list)
        sorted_list = sorted(values_list)
        
        rank = (0.50 * (count - 1)) + 1
        
        if rank.is_integer():
            percentile = sorted_list[math.floor(rank) - 1]
        else:
            percentile = sorted_list[math.floor(rank) - 1]
        
        return percentile

    def percentile_60(self, values_list):
        if type(values_list) is not list:
            raise ValueError

        count = len(values_list)
        sorted_list = sorted(values_list)
        
        rank = (0.60 * (count - 1)) + 1
        
        if rank.is_integer():
            percentile = sorted_list[math.floor(rank) - 1]
        else:
            percentile = sorted_list[math.floor(rank) - 1]
        
        return percentile

    def percentile_80(self, values_list):
        if type(values_list) is not list:
            raise ValueError

        count = len(values_list)
        sorted_list = sorted(values_list)
        
        rank = (0.80 * (count - 1)) + 1
        
        if rank.is_integer():
            percentile = sorted_list[math.floor(rank) - 1]
        else:
            percentile = sorted_list[math.floor(rank) - 1]
        
        return percentile

    # prints a given number of rows in the loaded dataset.
    # per the instructions on part 2, only 100, 1000 and 5000 rows can be printed and served
    # as options to the user.
    def print_rows(self):
        N = 0

        while N != 100 and N != 1000 and N != 5000:
            N = int(input("How many rows to display? (100|1000|5000): "))
        
        for row_index in range(0, N):
            for column in self.columns_as_lists:
                print(column[row_index], end = " ")
            
            print(end = "\n")

    # displays the questions and answers for part 4. (Analysis)
    # each question requires a problem to be solved in code, before the answer is displayed.
    def print_analysis(self):
        int_to_month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
        print("\n")

        print("1. What was the month of the year in 2019 with most delays overall? And how many delays were recorded in that month?")
        mode_of_month = self.mode(self.list_for_chosen_column(0))
        print(MAKE_YELLOW, "  The month with the most delays was "+ int_to_month[mode_of_month] +". There were delays recorded in that month.", RESET)

        print("2. What was the month of the year in 2019 with most delays overall? And how many delays were recorded in that day?")
        mode_of_month = self.mode(self.list_for_chosen_column(0))
        print(MAKE_YELLOW, "  The month with the most delays was "+ int_to_month[mode_of_month] +". There were delays recorded in that month.", RESET)

        print("3. What airline carrier experience the most delays in January, July and December")
        print(MAKE_YELLOW, "  Ans:", "<answer>", RESET)

        print("4. What was the average plane age of all planes with delays operated by American Airlines inc.")
        print(MAKE_YELLOW, "  Ans:", "<answer>", RESET)

        print("5. How many planes were delayed for more than 15 minutes during days with \"heavy snow\" (Days when the inches of snow on ground were 15 or more) )?")
        print(MAKE_YELLOW, "  Ans:", "<answer>", RESET)

        print("6. What are the 5 Airports that had the most delays in 2019?")
        print(MAKE_YELLOW, "  Ans:", "<answer>", RESET)

# Main Code
file = 'Airline_Delays_500_Lines.csv'
info = Airport(file) 

valid_input = False
active = True

# the main active loop of the program.
# the application musts stay active as long as the user
# does not opt out of the program by choice.
while(active):
    info.menu()

    end = input('\nWould you like to end the program? (y/n) ')

    if end == 'y' or input == 'Y' or input == 'Yes':
        print(MAKE_MAGENTA, '\nThank you for testing our program! :)\n', RESET)
        active = False








