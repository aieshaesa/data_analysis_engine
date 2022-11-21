#code to add to main file

import csv
import math

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

    def remove_punctuation(self):
        for i in range(len(self.columns_as_lists)):
            for j in range(len(self.columns_as_lists[i])):
                self.columns_as_lists[i][j] = self.columns_as_lists[i][j].replace('"', '')

        # this prints all carrier names, now without quotes
        """
        for i in range(self.size):
            if self.columns_as_lists[i][0] == 'CARRIER_NAME':
                for j in range(len(self.columns_as_lists[i])):
                    print(self.columns_as_lists[i][j])
        """
        
    def column_names(self):
        for i in range(self.size):
            print(i+1,":", self.columns_as_lists[i][0])
        print("\n")

    def menu(self):
        num = 0
        valid = False
        options = ['Drop a Column', 'Count Distinct Value', 'Search for a Value', 'Sort a Column', 'Mean of a Column', 
            'Median of a Column', 'Mode of a Column', 'Standard Deviation', 'Variance', 'Minimum', 'Maximum',
            '20 Percentile', '40 Percentile', '50 Percentile', '60 Percentile', '80 Percentile' ]
    
        for i in range(len(options)):
            print(num+1, ':', options[i])
            num += 1

        while(valid == False):
            ans = input('What would you like to do? ')
            ans = int(ans)
            ans -= 1
            if ans < 0 or ans > len(options):
                print('Number given isn\'t valid, please try again')
            else:
                valid = True
        
        choice = self.choose_column()
        choice = int(choice)
        
        if ans == 0:
            self.drop_column(choice)
        elif ans == 1:
            self.count_distinct_value(choice)
        elif ans == 4:
            self.mean(choice)
        elif ans == 5:
            self.median(choice)
        elif ans == 6:
            self.mode(choice)
        elif ans == 7:
            self.standard_deviation(choice)
        elif ans == 8:
            self.variance(choice, False, 0)
        elif ans == 9:
            self.minimum(choice)
        elif ans == 10:
            self.maximum(choice)
        elif ans == 11:
            self.percentile_20(choice)
        elif ans == 12:
            self.percentile_40(choice)
        elif ans == 13:
            self.percentile_50(choice)
        elif ans == 14:
            self.percentile_60(choice)
        elif ans == 15:
            self.percentile_80(choice)
        """
        elif ans == 2:
            self.search_value(choice)
        elif ans == 3:
            self.sort_column(choice)

        """

    def unique(self, column):
        return set(column)

    def drop_column(self, column):
        valid = False
        while(valid == False):
            ans = input('Enter the number of the column you\'d like to drop: ')
            if int(ans) < 1 or int(ans) > self.size:
                print('Number given isn\'t valid, please try again')
            else:
                valid = True

        drop = int(ans)
        self.columns_as_lists.pop(drop-1)
        self.size = len(self.columns_as_lists)
        #rows = int(len(self.columns_as_lists[0]))
        #print("size of rows: ", rows)
        #print("new size is: ", self.size)

    def choose_column(self):
        valid = False
        self.column_names()

        while(valid == False):
            column = input('Enter the number of the column of you\'re choosing: ')
            column = int(column)
            column -= 1
            if column < 0 or column > self.size:
                print('Number given isn\'t valid, please try again')
            else:
                valid = True

        return column
        
    def list_for_chosen_column(self, number):
        column = []
        for i in range(1, len(self.columns_as_lists[number])):
            try:
                column.append(int(self.columns_as_lists[number][i]))
            except:
                break

        for i in range(1, len(self.columns_as_lists[number])):   
            try:
                column.append(float(self.columns_as_lists[number][i]))
            except:
                print('The column you chose does not include integers or floats')
                return False

        return column

    def count_distinct_value(self, column):
        column = self.choose_column()      
        valid = False
        count = 0

        for i in range(self.size):
            if i == column:
                print('The distinct values of', self.columns_as_lists[i][0], 'are: ')
                distinct_list = self.unique(self.columns_as_lists[i][1:])
                num = 0
                for value in distinct_list:
                    print(num+1, ':', value)
                    num += 1

                while(valid == False):
                    choice = input('Which value would you like to count? ')
                    choice = int(choice)
                    choice -= 1
                    if choice < 0 or choice > num+1:
                        print('Number given isn\'t valid, please try again')
                    else:
                        num = 0
                        for value in distinct_list:
                            num += 1
                            if num == choice+1:
                                distinct = value
                        valid = True

                for i in range(len(self.columns_as_lists[column])):
                    if self.columns_as_lists[column][i] == distinct:
                        count += 1

                print('The amount of times', distinct, 'is in the data is', count, 'times.')
    
    def mean(self, number):
        sum = 0
        chosen_column = self.list_for_chosen_column(number)
        # if column chosen doesn't include integers, the function will stop
        if chosen_column == False:
            return 0

        for i in range(len(chosen_column)):
            sum = sum + chosen_column[i]

        mean = (sum / len(chosen_column))
        print('The mean of the column', self.columns_as_lists[number][0], 'is:', mean)

    def median(self, number):
        chosen_column = self.list_for_chosen_column(number)
        if chosen_column == False:
            return 0
        count = len(chosen_column)
        sorted_list = sorted(chosen_column)

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

        print('The median of the column', self.columns_as_lists[number][0], 'is:', median)

    def mode(self, number):
        chosen_column = self.list_for_chosen_column(number)
        if chosen_column == False:
            return 0
        sorted_list = sorted(chosen_column) # list must be sorted in ascending order. Auto-sort the list.
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

        print('The mode of the column', self.columns_as_lists[number][0], 'is:', mode)

    def standard_deviation(self, number):
        chosen_column = self.list_for_chosen_column(number)
        list_variance = self.variance(0, True, chosen_column)

        # the square root of the variance is the standard deviation.
        standard_deviation = math.sqrt(list_variance)

        print('The standard deviation of the column', self.columns_as_lists[number][0], 'is:', standard_deviation)

    def variance(self, number, sd, number_list):
        if(sd == False):
            chosen_column = self.list_for_chosen_column(number)
            if chosen_column == False:
                return 0
            count = len(chosen_column)
            difference = 0
            
            for num in chosen_column:
                # for each number, substract it by the mean of the list, then square it, and add it to the difference.
                difference = difference + (num - self.mean(chosen_column)) ** 2
            
            variance = difference / count
            print('The variance of the column', self.columns_as_lists[number][0], 'is:', variance)
        else:
            count = len(number_list)
            difference = 0
            
            for num in number_list:
                # for each number, substract it by the mean of the list, then square it, and add it to the difference.
                difference = difference + (num - self.mean(number_list)) ** 2
            
            variance = difference / count

        return variance

    def minimum(self, number):
        chosen_column = self.list_for_chosen_column(number)
        if chosen_column == False:
            return 0
        minimum = min(chosen_column)
        print('The minimum of the column', self.columns_as_lists[number][0], 'is:', minimum)

    def maximum(self, number):
        chosen_column = self.list_for_chosen_column(number)
        if chosen_column == False:
            return 0
        maximum = min(chosen_column)
        print('The maximum of the column', self.columns_as_lists[number][0], 'is:', maximum)

    def percentile_20(self, number):
        chosen_column = self.list_for_chosen_column(number)
        if chosen_column == False:
            return 0
        count = len(chosen_column)
        sorted_list = sorted(chosen_column)
        
        # calculate the percentile, as the 'rank'.
        rank = (0.20 * (count - 1)) + 1
        
        # if rank is an integer, then use the rank as an index and get the value at that index.
        if rank.is_integer():
            percentile = sorted_list[math.floor(rank) - 1]
        else:
            # if rank is a float, then get the value at that index as a integer, then add the rank's 
            # part to its whole part, as the percentile. 
            # We thought we had to return the actual value in the array, instead of a float, so we return that as well.
            percentile = sorted_list[math.floor(rank) - 1]
        
        print('The 20th percentile of the column', self.columns_as_lists[number][0], 'is:', percentile)

    def percentile_40(self, number):
        chosen_column = self.list_for_chosen_column(number)
        if chosen_column == False:
            return 0
        count = len(chosen_column)
        sorted_list = sorted(chosen_column)
        
        # calculate the percentile, as the 'rank'.
        rank = (0.40 * (count - 1)) + 1
        
        # if rank is an integer, then use the rank as an index and get the value at that index.
        if rank.is_integer():
            percentile = sorted_list[math.floor(rank) - 1]
        else:
            # if rank is a float, then get the value at that index as a integer, then add the rank's 
            # part to its whole part, as the percentile. 
            # We thought we had to return the actual value in the array, instead of a float, so we return that as well.
            percentile = sorted_list[math.floor(rank) - 1]
        
        print('The 40th percentile of the column', self.columns_as_lists[number][0], 'is:', percentile)

    def percentile_50(self, number):
        chosen_column = self.list_for_chosen_column(number)
        if chosen_column == False:
            return 0
        count = len(chosen_column)
        sorted_list = sorted(chosen_column)
        
        # calculate the percentile, as the 'rank'.
        rank = (0.50 * (count - 1)) + 1
        
        # if rank is an integer, then use the rank as an index and get the value at that index.
        if rank.is_integer():
            percentile = sorted_list[math.floor(rank) - 1]
        else:
            # if rank is a float, then get the value at that index as a integer, then add the rank's 
            # part to its whole part, as the percentile. 
            # We thought we had to return the actual value in the array, instead of a float, so we return that as well.
            percentile = sorted_list[math.floor(rank) - 1]
        
        print('The 50th percentile of the column', self.columns_as_lists[number][0], 'is:', percentile)

    def percentile_60(self, number):
        chosen_column = self.list_for_chosen_column(number)
        if chosen_column == False:
            return 0
        count = len(chosen_column)
        sorted_list = sorted(chosen_column)
        
        # calculate the percentile, as the 'rank'.
        rank = (0.60 * (count - 1)) + 1
        
        # if rank is an integer, then use the rank as an index and get the value at that index.
        if rank.is_integer():
            percentile = sorted_list[math.floor(rank) - 1]
        else:
            # if rank is a float, then get the value at that index as a integer, then add the rank's 
            # part to its whole part, as the percentile. 
            # We thought we had to return the actual value in the array, instead of a float, so we return that as well.
            percentile = sorted_list[math.floor(rank) - 1]
        
        print('The 60th percentile of the column', self.columns_as_lists[number][0], 'is:', percentile)

    def percentile_80(self, number):
        chosen_column = self.list_for_chosen_column(number)
        if chosen_column == False:
            return 0
        count = len(chosen_column)
        sorted_list = sorted(chosen_column)
        
        # calculate the percentile, as the 'rank'.
        rank = (0.80 * (count - 1)) + 1
        
        # if rank is an integer, then use the rank as an index and get the value at that index.
        if rank.is_integer():
            percentile = sorted_list[math.floor(rank) - 1]
        else:
            # if rank is a float, then get the value at that index as a integer, then add the rank's 
            # part to its whole part, as the percentile. 
            # We thought we had to return the actual value in the array, instead of a float, so we return that as well.
            percentile = sorted_list[math.floor(rank) - 1]
        
        print('The 80th percentile of the column', self.columns_as_lists[number][0], 'is:', percentile)


# Main Code
file = 'Airline_Delays_500_Lines.csv'
info = Airport(file) 

valid_input = False
active = True

while(active):
    info.menu()

    end = input('\nWould you like to end the program? (y/n) ')
    if end == 'y' or input == 'Y' or input == 'Yes':
        print('\nThank you for testing our program! :)\n')
        active = False


"""
    num = 1
    for value in info.column:
        print(num, ' - ', info.column[num-1])
        num += 1

for i in range(info.size):
    # print each column
    print(info.columns_as_lists[i])  # All the values in the first column of your CSV
"""
        # print total number of columns
"""
        print("Total columns:", self.size)

        for i in range(self.size):
            print(i,":", self.columns_as_lists[i][0])
        print("\n")
"""