# code to add to main file
# 11/21/2022

import os
import csv
import math
import datetime
from collections import Counter

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
    chosen_column = []
    column = []
    size = 0
    filename = ""


    def file_input(self):
        fileList = []
        good_file = False
        #file = 'Airline_Delays_500_Lines.csv'
        for x in os.listdir():
            if x.endswith(".csv"):
                # Prints only text file present in My Folder
                fileList.append(x)
        while good_file == False:
            for idx,i in enumerate(fileList):
                print(idx+1,":",i)
            time = self.get_time()
            print("[", time, "] Please choose the number of the file to load:")
            file = input()
            for idx,i in enumerate(fileList):
                #print(file,"-->", idx)
                if file == str(idx+1):
                    good_file = True
                    file = i
        return file
    

    def load_file(self, file):
        missing = "NONE"
        start = self.get_time()

        with open(file) as csv_file:
            # creating an object of csv reader
            # with the delimiter
            csv_reader = csv.reader(csv_file, delimiter = ',')
        
            # loop to iterate through the rows of csv
            for row in csv_reader:
                found_none = False
                # adding first row
                for field in row:
                    if field == missing:
                        found_none = True
                        break
                if found_none == False:
                    if row not in self.column:
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

        end = self.get_time()
        total_time = end - start

        return total_time

    # prints the menu to the terminal that servers as the main interface to the user.
    # all the options listed are the ones that are valid to choose from.
    # not all actions can be made towards particular columns, so exceptions must be raised to prevent errors.    
    def menu(self):
        ans = 0
        ##############################[ User Actions ]##############################
        while(ans != 3):
            valid = False
            options = ['Load Data', 'Exploring Data', 'Data Analysis', 'Quit']
            options_length = len(options)

            exploring_options = ['List All Columns', 'Drop Columns', 'Describe Columns', 
                'Search Element in Column', 'Count Distinct Value', 'Sort Column', 
                'Print first 100, 1000, or 5000 Rows', 'Back to Main Menu']
            exploring_options_length = len(exploring_options)

            try: 
                print(MAKE_BLUE, '\nMain Menu:\n**********', RESET)

                for i in range(options_length):
                    print(MAKE_BLUE, '(', i+1, ') ', options[i], RESET)

                while(valid == False):
                    print(MAKE_CYAN, '\nWhat would you like to do? (1 - '+ str(options_length) +'): ', RESET)
                    ans = int(input())
                    if ans < 1 or ans > options_length:
                        print(MAKE_RED, 'Number given isn\'t valid, please try again', RESET)
                    else:
                        valid = True
                # this is so that the answer follows the list counting system which starts at 0
                ans -= 1

                ##############################[ User Actions ]##############################

                # Load Data Set
                if ans == 0:
                    print(MAKE_BLUE, '\nLoad data set:\n**************', RESET)

                    self.filename = self.file_input()
                    time = self.get_time()
                    total_time = self.load_file(self.filename)

                    time = self.get_time()
                    total_columns = len(self.columns_as_lists)
                    print(MAKE_GREEN, "[", time, "] Total Columns Read: ", total_columns, RESET)

                    time = self.get_time()
                    total_rows = len(self.columns_as_lists[0])
                    print(MAKE_GREEN, "[", time, "] Total Rows Read: ", total_rows, RESET)

                    print(MAKE_YELLOW, "File loaded successfully! time to load ", total_time, RESET)

                # Exploring Data
                if ans == 1 and self.filename != "":
                    print('\n')
                    choice = 0
                    while(choice != 7):
                        valid = False
                        print(MAKE_BLUE, '\n(', ans+1, ') ', options[ans], ':\n************************', RESET)

                        for i in range(exploring_options_length):
                            print(MAKE_BLUE, '(', i+1, ') ', exploring_options[i], RESET)

                        while(valid == False):
                            print(MAKE_CYAN, '\nWhat would you like to do? (1 - '+ str(exploring_options_length) +'): ', RESET)
                            choice = int(input())

                            if choice < 1 or choice > exploring_options_length:
                                print(MAKE_RED, 'Number given isn\'t valid, please try again', RESET)
                            else:
                                valid = True

                        choice -= 1
                        
                        # list all columns
                        if choice == 0:
                            print(MAKE_BLUE, '\n(', choice+1, ') ', exploring_options[choice], ': ****************', RESET)

                            self.print_column_names()
                        
                        # drop columns
                        if choice == 1:
                            print(MAKE_BLUE, '\n(', choice+1, ') ', exploring_options[choice], ': \n****************', RESET)

                            if self.size <= 1:
                                raise Exception("At least 1 column must remain in the dataset.")
                            
                            option = 0
                            self.print_column_names()

                            while option < 1 or option > self.size:
                                print(MAKE_CYAN, "Enter a column to drop (1 - "+ str(self.size) +"): ", RESET)
                                option = int(input())

                            column_dropped_header = self.columns_as_lists[option-1][0]
                            self.drop_column(option)

                            print(MAKE_GREEN, 'Column', column_dropped_header, 'was dropped.', RESET)
                        
                        # describe columns
                        if choice == 2:
                            print(MAKE_BLUE, '\n(', choice+1, ') ', exploring_options[choice], ': \n**********************', RESET)
                            
                            option = self.choose_column()

                            chosen_column_header = self.columns_as_lists[option][0]
                            self.list_for_chosen_column(option)

                            time = self.get_time()
                            start = time
                            print(MAKE_GREEN, "[", time, "]", chosen_column_header, RESET)
                            print(MAKE_GREEN, "\nColumn Stats:\n==============", RESET)

                            print(MAKE_GREEN, "Count: ", len(self.chosen_column), RESET)
                            print(MAKE_GREEN, "Unique: ", self.unique(self.chosen_column), RESET)

                            mean = self.mean(self.chosen_column)
                            if mean == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine mean.', RESET)
                            else:
                                print(MAKE_GREEN, "Mean: ", mean, RESET)

                            median = self.median(self.chosen_column)
                            if median == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine median.', RESET)
                            else:
                                print(MAKE_GREEN, "Median: ", median, RESET)

                            mode = self.mode(self.chosen_column)
                            if mode == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine mode.', RESET)
                            else:
                                print(MAKE_GREEN, "Mode: ", mode, RESET)

                            sd = self.standard_deviation(self.chosen_column)
                            if sd == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine standard deviation.', RESET)
                            else:
                                print(MAKE_GREEN, "Standard Deviation (SD): ", sd, RESET)
                            
                            variance = self.variance(self.chosen_column)
                            if variance == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine variance.', RESET)
                            else:
                                print(MAKE_GREEN, "Variance: ", variance, RESET)

                            min = self.minimum(self.chosen_column)
                            if min == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine minimum.', RESET)
                            else:
                                print(MAKE_GREEN, "Minimum: ", min, RESET)    

                            max = self.maximum(self.chosen_column)
                            if max == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine maximum.', RESET)
                            else:
                                print(MAKE_GREEN, "Maximum: ", max, RESET)   

                            per20 = self.percentile_20(self.chosen_column)
                            if per20 == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine 20th percentile.', RESET)
                            else:
                                print(MAKE_GREEN, "20 Percentile (P20): ", per20, RESET)   

                            per40 = self.percentile_40(self.chosen_column)
                            if per40 == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine 40th percentile.', RESET)
                            else:
                                print(MAKE_GREEN, "40 Percentile (P40): ", per40, RESET)

                            per50 = self.percentile_50(self.chosen_column)
                            if per50 == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine 50th percentile.', RESET)
                            else:
                                print(MAKE_GREEN, "50 Percentile (P50): ", per50, RESET)

                            per60 = self.percentile_60(self.chosen_column)
                            if per60 == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine 60th percentile.', RESET)
                            else:
                                print(MAKE_GREEN, "60 Percentile (P60): ", per60, RESET)

                            per80 = self.percentile_80(self.chosen_column)
                            if per80 == False:
                                print(MAKE_RED, 'The column you chose does not include data that can determine 80th percentile.', RESET)
                            else:
                                print(MAKE_GREEN, "80 Percentile (P80): ", per80, RESET)

                            end = self.get_time()

                            total_time = end - start
                            print(MAKE_YELLOW, "Stats printed successfully! time to process is ", total_time, RESET)

                        # search element in column
                        if choice == 3 and self.filename != "":
                            print(MAKE_BLUE, '(', choice+1, ') ', exploring_options[choice], '\n****************', RESET)
                            
                            option = self.choose_column()

                            chosen_column_header = self.columns_as_lists[option][0]
                            for i in range(self.size):
                                if i == option:
                                    print(MAKE_CYAN, 'The distinct values of', self.columns_as_lists[i][0], 'are: ', RESET)
                                    distinct_list = self.unique(self.columns_as_lists[i][1:])

                                    for value in distinct_list:
                                        print(MAKE_MAGENTA, value, RESET)

                            self.list_for_chosen_column(option)
                            count = 0

                            print(MAKE_CYAN, 'Enter element to Search: \n', RESET)
                            value = input()
                            start = self.get_time()
                            # three for loops with try blocks so that ints, floats, and strings
                            # will be counted
                            for i in range(len(self.chosen_column)):   
                                try:
                                    if int(value) == self.chosen_column[i]:
                                        count += 1
                                except:
                                    break

                            if count < 1:
                                for i in range(len(self.chosen_column)):
                                    try:
                                        if float(value) == self.chosen_column[i]:
                                            count += 1
                                    except:
                                        break
                            if count < 1:
                                for i in range(len(self.chosen_column)):
                                    try:
                                        if value == self.chosen_column[i]:
                                            count += 1
                                    except:
                                        break
                            
                            end = self.get_time()
                            total_time = end - start
                            if count > 0:
                                print(MAKE_GREEN, '[', total_time, ']', value, 'was found', count, 'times.', RESET)
                                print(MAKE_YELLOW, 'Search was successful! time to search was ', total_time, RESET)
                            else:
                                print(MAKE_RED, '[', time, '] Element was not found, search unsuccessful', RESET)
                            
                            print('\n')

                        # count distinct value
                        if choice == 4:
                            column_number = self.choose_column()
                            self.list_for_chosen_column(column_number)
                            unique_list = self.unique(self.chosen_column)
                            index = 0
                            option = -1

                            for value in unique_list:
                                index += 1
                                print(MAKE_MAGENTA, index, ":", value, RESET)
                                    
                            while option < 1 or option > index:
                                print(MAKE_CYAN, "Which value would you like to count? (1 - "+ str(index) +"): ", RESET)
                                option = int(input())
                                    
                            total_time, distinct_value, count = self.count_distinct_value(column_number, unique_list[option - 1])
                            if count > 0:
                                print(MAKE_GREEN, '[', time, '] The amount of times', distinct_value, 'is in the data is', count, 'time(s).', RESET)
                                print(MAKE_YELLOW, 'Total time to count distinct value ', total_time, RESET)
                            else:
                                print(MAKE_RED, '[', time, '] Element was not found in data', RESET)

                        # sort column
                        if choice == 5:
                            print(MAKE_BLUE, '(', choice+1, ') ', exploring_options[choice], ':\n********************', RESET)

                            num = self.choose_column()
                            self.sort_column(num)
                        
                        # print first 100, 1000, or 5000 rows
                        if choice == 6:
                            print(MAKE_BLUE, '(', choice+1, ') ', exploring_options[choice], ':\n********************', RESET)

                            self.print_rows()


                #analysis
                if ans == 2 and self.filename != "":
                    print(MAKE_BLUE, '(', ans+1, ') ', exploring_options[ans], ':\n******************************', RESET)
                    self.print_analysis()

                if ans == 3:
                    print(MAKE_MAGENTA, '\nThank you for testing our program! :)\n', RESET)

                if ans > 0 and ans < 3 and self.filename == "":
                    print(MAKE_RED, "LOAD DATA REQUIRED", RESET)  

            except ValueError:
                print(MAKE_RED, 'The column you chose does not include integers or floats for this action.', RESET)

            except Exception as ex:
                print(MAKE_RED, ex, RESET)

        ############################################################################

    # returns the current date and time
    def get_time(self):
        time = datetime.datetime.utcnow()
        return time

    # prints each column in the dataset to the terminal.
    # this is needed to show options to the user which columns are available to work with.
    def print_column_names(self):
        for i in range(self.size):
            print(MAKE_MAGENTA, i+1,":", self.columns_as_lists[i][0], RESET)

        print("\n")

    def print_result(self, function, column, result):
        print(MAKE_GREEN, 'The ', function, ' of the column ', column, ' is ', result, RESET)

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

    # sorts a column given a choice of a column number.
    # checking if a column is numerical is needed to sort only numbers or only strings as keys.
    def sort_column(self, column_choice):
        column_chosen = self.columns_as_lists[column_choice]
        copy_of_column_chosen = column_chosen[1:]

        option = None

        while option != "asc" and option != "desc":
            print(MAKE_CYAN, "Which sort order use? (asc|desc): ", RESET)
            option = input()

        if self.column_is_numerical(column_chosen):
            # ascending order
            if option == "asc":
                copy_of_column_chosen.sort(key = float)
                column_chosen[1:] = copy_of_column_chosen

                print(MAKE_GREEN, "Column " + column_chosen[0] + " sorted in ascending order.", RESET)

            # descending order
            elif option == "desc":
                copy_of_column_chosen.sort(reverse = True, key = float)
                column_chosen[1:] = copy_of_column_chosen

                print(MAKE_GREEN, "Column " + column_chosen[0] + " sorted in descending order.", RESET)
        else:
            # ascending order
            if option == "asc":
                copy_of_column_chosen.sort(key = str)
                column_chosen[1:] = copy_of_column_chosen

                print(MAKE_GREEN, "Column " + column_chosen[0] + " sorted in ascending order.", RESET)

            # descending order
            elif option == "desc":
                copy_of_column_chosen.sort(reverse = True, key = str)
                column_chosen[1:] = copy_of_column_chosen

                print(MAKE_GREEN, "Column " + column_chosen[0] + " sorted in descending order.", RESET)
        
        print(MAKE_GREEN, copy_of_column_chosen, RESET)
            

    # deletes a column from loaded dataset.
    # all the columns in the dataset are the only valid ones to be deleted,
    # and all other choices outside this range are invalid and disregarded.
    def drop_column(self, column_number):
        self.columns_as_lists.pop(column_number-1)
        self.size = len(self.columns_as_lists)

    # prints all columns to the user so they can choose which they'd like to use
    def choose_column(self):
        option = 0
        time = self.get_time()
        self.print_column_names()
        while option < 1 or option > self.size:
            print(MAKE_CYAN, "[", time, "] Enter Column Number (1 - "+ str(self.size) +"): \n", RESET)
            option = int(input())

        return option-1
    
    # converts a raw column set to either a list or a dictionary.
    # column headers are stripped away so indexing doesn't include the column header.
    # it convert a column into a numerically indexed list regardless if the given column is numerical or not.
    # returns: a list or dictionary of a given column.
    def list_for_chosen_column(self, number):
        self.chosen_column = []
        is_number = False
        for i in range(1, len(self.columns_as_lists[number])):
            try:
                self.chosen_column.append(int(self.columns_as_lists[number][i]))
                is_number = True
            except:
                break

        if is_number == False:
            for i in range(1, len(self.columns_as_lists[number])):   
                try:
                    self.chosen_column.append(float(self.columns_as_lists[number][i]))
                    is_number = True
                except:
                    break
        
        if is_number == False:
            for i in range(1, len(self.columns_as_lists[number])):
                self.chosen_column.append(self.columns_as_lists[number][i])
                
            return False
    

    # retrieves the number of occurences of a value in a given column.
    # it first checks if a column is numerical or not to make sure it's comparing
    # numbers to numbers and strings to strings.
    # returns: the value to look for, and the count as the result.
    def count_distinct_value(self, column_number, value_to_look):
        start = self.get_time()
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
        end = self.get_time()
        total_time = end - start

        return total_time, value_to_look, count


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
        try:
            sum = 0
            mean = None

            for i in range(len(values_list)):
                sum = sum + values_list[i]

            mean = (sum / len(values_list))
            
            return mean

        except:
            return False

    # returns the median of a generic list.
    def median(self, values_list):
        #if type(values_list) is not list:
        #    raise ValueError
            
        try:
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
        
        except:
            return False

    # returns the mode of a generic list.
    def mode(self, values_list):
        #if type(values_list) is not list:
        #    raise ValueError
        try:
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
        
        except:
            return False

    # returns the standard deviation of a generic list.
    # the standard deviation is the square root of the variance, 
    # so variance function must be used for the calculation.
    def standard_deviation(self, values_list):
        #if type(values_list) is not list:
        #    raise ValueError
        try:
            list_variance = self.variance(values_list)
            standard_deviation = list_variance ** 0.5

            return standard_deviation

        except:
            return False

    # returns the variance of a generic list.
    # each item in the list must be calculated in order to
    # calculate the variance overall.
    def variance(self, values_list):
        #if type(values_list) is not list:
        #    raise ValueError
        try:
            variance = 0
            difference = 0

            list_mean = self.mean(values_list)
            
            for num in values_list:
                # for each number, substract it by the mean of the list, then square it, and add it to the difference.
                difference = difference + (num - list_mean) ** 2
            
            variance = difference / len(values_list)

            return variance
        
        except:
            return False

    # returns the minimum value contained in a given generic list.
    def minimum(self, values_list):
        #if type(values_list) is not list:
        #    raise ValueError
        try:
            minimum = min(values_list)
            return minimum

        except:
            return False

    # returns the maximum value contained in a given generic list.
    def maximum(self, values_list):
        #if type(values_list) is not list:
            #raise ValueError
        try:
            maximum = max(values_list)
            return maximum
        
        except:
            return False

    ### percentile_20, percentile_40, percentile_50, percentile_60, percentile_80 ###
    # returns the value at the 20th, 40th, 60th and 80th percentile of a given generic list.
    def percentile_20(self, values_list):
        #if type(values_list) is not list:
            #raise ValueError
        try:
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
        
        except:
            return False

    def percentile_40(self, values_list):
        #if type(values_list) is not list:
        #    raise ValueError
        try:
            count = len(values_list)
            sorted_list = sorted(values_list)
            
            rank = (0.40 * (count - 1)) + 1
            
            if rank.is_integer():
                percentile = sorted_list[math.floor(rank) - 1]
            else:
                percentile = sorted_list[math.floor(rank) - 1]
            
            return percentile

        except:
            return False

    def percentile_50(self, values_list):
        #if type(values_list) is not list:
        #    raise ValueError
        try:
            count = len(values_list)
            sorted_list = sorted(values_list)
            
            rank = (0.50 * (count - 1)) + 1
            
            if rank.is_integer():
                percentile = sorted_list[math.floor(rank) - 1]
            else:
                percentile = sorted_list[math.floor(rank) - 1]
            
            return percentile

        except:
            return False

    def percentile_60(self, values_list):
        #if type(values_list) is not list:
        #    raise ValueError
        try:
            count = len(values_list)
            sorted_list = sorted(values_list)
            
            rank = (0.60 * (count - 1)) + 1
            
            if rank.is_integer():
                percentile = sorted_list[math.floor(rank) - 1]
            else:
                percentile = sorted_list[math.floor(rank) - 1]
            
            return percentile

        except:
            return False

    def percentile_80(self, values_list):
        #if type(values_list) is not list:
        #    raise ValueError
        try:
            count = len(values_list)
            sorted_list = sorted(values_list)
            
            rank = (0.80 * (count - 1)) + 1
            
            if rank.is_integer():
                percentile = sorted_list[math.floor(rank) - 1]
            else:
                percentile = sorted_list[math.floor(rank) - 1]
            
            return percentile

        except:
            return False

    # prints a given number of rows in the loaded dataset.
    # per the instructions on part 2, only 100, 1000 and 5000 rows can be printed and served
    # as options to the user.
    def print_rows(self):
        N = 0

        while N != 100 and N != 1000 and N != 5000:
            print(MAKE_CYAN, "How many rows to display? (100|1000|5000): ", RESET)
            N = int(input())
        for row_index in range(0, N):
            for column in self.columns_as_lists:
                print(MAKE_GREEN, column[row_index], end = " ")
            
            print(end = "\n")

    # function to answer analysis question 6
    def most_frequent(self, values):
        counter = 0
        num = values[0]

        for i in values:
            curr_freq = values.count(i)
            if(curr_freq > counter):
                counter = curr_freq
                num = i
        
        return num


    # displays the questions and answers for part 4. (Analysis)
    # each question requires a problem to be solved in code, before the answer is displayed.
    def print_analysis(self):
        int_to_month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
        print("\n")

        print("1. How many airlines are included in the data set? Print the first 5 in alphabetical order.")
        first5Distinct = self.unique(self.columns_as_lists[8][1:])

        print(MAKE_YELLOW, "There are", len(first5Distinct), "airlines in the dataset. The first 5 are:", RESET)
        first5Distinct.sort()

        for index in range(5):
            print(MAKE_YELLOW, "-", first5Distinct[index], RESET)

        print("\n2. How many departing airports are included in the data set? Print the last 5 in alphabetical order.")

        last5Distinct = self.unique(self.columns_as_lists[17][1:])

        print(MAKE_YELLOW, "There are", len(last5Distinct), "departing airports in the dataset. The last 5 are:", RESET)

        last5Distinct = last5Distinct[len(last5Distinct)-6:len(last5Distinct) - 1]
        last5Distinct.sort()

        for index in range(5):
            print(MAKE_YELLOW, "-", last5Distinct[index], RESET)

        print("\n3. What airline has the oldest plane? Print the 5 airlines that have the 5 oldest planes recorded.")
        plane_ages = {}

        for index in range(1, self.size):
            airline = self.columns_as_lists[8][index]
            age = int(self.columns_as_lists[16][index])

            if airline in plane_ages:
                if age > plane_ages[airline]:
                    plane_ages[airline] = age
            else:
                plane_ages[airline] = age
        
        plane_ages = sorted(plane_ages.items(), reverse = True, key = lambda pair: pair[1])
        print(MAKE_YELLOW, plane_ages[0][0], "has the oldest plane. The 5 airlines with the 5 oldest planes are:", RESET)

        for index in range(5):
            print(MAKE_YELLOW, "-", plane_ages[index][0], RESET)


        print("\n4. What is the airport that averaged the greatest number of passengers recorded in 2019? Print the 5 airport that averaged the greatest number of passengers in 2019.")
        airport_avg_pasn = {}

        for index in range(1, self.size):
            airline = self.columns_as_lists[8][index]
            avg_pasn = int(self.columns_as_lists[12][index])

            if airline in airport_avg_pasn:
                if avg_pasn > airport_avg_pasn[airline]:
                    airport_avg_pasn[airline] = avg_pasn
            else:
                airport_avg_pasn[airline] = avg_pasn

        airport_avg_pasn = sorted(airport_avg_pasn.items(), reverse = True, key = lambda pair: pair[1])
        print(MAKE_YELLOW, "The airport with the highest average number of passengers was", airport_avg_pasn[0][0], RESET)
        print(MAKE_YELLOW, "The airport with the highest avg. passengers are:", RESET)

        for index in range(5):
            print(MAKE_YELLOW, "-", airport_avg_pasn[index][0], RESET)
        
        print("\n5. What is the airline that averaged the greatest number of employees (Flight attendants and ground service) in 2019? Print the 5 airlines that averaged the greatest number of employees in 2019.")
        airport_avg_empl = {}

        for index in range(1, self.size):
            airline = self.columns_as_lists[8][index]
            avg_atten_grnd_sum = float(self.columns_as_lists[15][index]) + float(self.columns_as_lists[14][index])

            if airline in airport_avg_empl:
                if avg_atten_grnd_sum > airport_avg_empl[airline]:
                    airport_avg_empl[airline] = avg_atten_grnd_sum
            else:
                airport_avg_empl[airline] = avg_atten_grnd_sum

        airport_avg_empl = sorted(airport_avg_empl.items(), reverse = True, key = lambda pair: pair[1])
        print(MAKE_YELLOW, airport_avg_empl[0][0], "was the airline with the greatest avg. of employees.", RESET)
        print(MAKE_YELLOW, "The 5 airlines with the highest avg. of employees are:", RESET)

        for index in range(5):
            print(MAKE_YELLOW, "-", airport_avg_empl[index][0], RESET)

        print("\n6. What was the month of the year in 2019 with most delays overall? And how many delays were recorded in that month?")
        mode_of_month = self.mode(self.columns_as_lists[2])
        month_of_mode_int = 1
        num_of_delays_month = 0

        for index in range(1, self.size):
            if self.columns_as_lists[2][index] == mode_of_month:
                month_of_mode_int = int(self.columns_as_lists[0][index])
                num_of_delays_month += 1

        print(MAKE_YELLOW, "The month with the most delays overall is", int_to_month[month_of_mode_int], "and there were", num_of_delays_month, "delays that month.", RESET)

        
        print("\n7. What was the day of the year in 2019 with most delays overall? And how many delays were recorded in that day?")
        delays = self.columns_as_lists[2][1:]
        month = []
        days = []
        List = []
        List2 = []
        List3 = []
        List4 = []
        for idx,i in enumerate(delays):
            if i == '1' and idx != 0:
                days.append(self.columns_as_lists[1][idx])
        most_delays = max(k for k,v in Counter(days).items() if v>1)
        
        print(MAKE_YELLOW,"The day of the week with the most delays was day", most_delays, "and there were", days.count(str(most_delays)),"delays.", RESET)

        print("\n8. What airline carrier experience the most delays in January, July and December")
        airlines_most = {}

        for index in range(1, self.size):
            int_month = self.columns_as_lists[0][index]
            airline = self.columns_as_lists[8][index]

            if (int_month == "1" or int_month == "7" or int_month == "12"):
                if airline in airlines_most:
                    airlines_most[airline] += 1
                else:
                    airlines_most[airline] = 1

        airlines_most = sorted(airlines_most.items(), key = lambda pair: pair[1], reverse = True)
        print(MAKE_YELLOW, airlines_most[0][0], "had the most delays in January, July and December.", RESET)

        print("\n9. What was the average plane age of all planes with delays operated by American Airlines inc.")
        plane_ages = []

        for index in range(1, self.size):
            if self.columns_as_lists[8][index] == "American Airlines Inc.":
                plane_ages.append(int(self.columns_as_lists[16][index]))

        print(MAKE_YELLOW, "The average plane age operated by American Airlines Inc. is", self.mean(plane_ages), RESET)
        
        print("\n10. How many planes were delayed for more than 15 minutes during days with \"heavy snow\" (Days when the inches of snow on ground were 15 or more) )?")
        plane_count = 0

        for index in range(1, len(self.columns_as_lists)):
            if self.columns_as_lists[2][index] == "1" and float(self.columns_as_lists[21][index]) > 0.15:
                plane_count += 1


        print(MAKE_YELLOW, "There were", plane_count, "planes that were delayed for more than 15 minutes in days with heavy snow.", RESET)

        print("\n11. What are the 5 airports (Departing Airports) that had the most delays in 2019? Print the airports and the number of delays")
        print(MAKE_YELLOW, "The 5 departing airports with the most delays are:", RESET)

        departing_airports_unique = self.unique(self.columns_as_lists[17][1:])
        first_5_most_delays = []

        for airport in departing_airports_unique:
            first_5_most_delays.append(self.count_distinct_value(17, airport))
        
        first_5_most_delays.sort(reverse = True, key = lambda tup: tup[1])
        
        for i in range(5):
            print(MAKE_YELLOW, "-", first_5_most_delays[i][1], "-", first_5_most_delays[i][2], "delays.", RESET)
# Main Code
info = Airport() 

info.menu()
