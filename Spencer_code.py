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

import csv # use the CSV library
import math # use the math library

##########[ Part 3 Functions ##########

################# UNIQUE FUNCTION ######################
# Returns unique values in list
def Unique(List):
    return set(List)

#####################################################

# Returns the count of whatever List is passed in.
def count_list(number_list):
    return len(number_list)

# Returns the mean/average of the passed list of numbers.
def mean(number_list):
    list_sum = sum(number_list)
    length = count_list(number_list)

    return list_sum / length

# Returns the mode of a list. It reads a sorted (ascending) list of numbers to get its mode.
# it will record a total of same numbers iterated over in the list, until it hits a new number,
# where the total resets to 1 again. The last number that has more occurrences of itself is returned.
def mode(number_list):
    sorted_list = sorted(number_list) # list must be sorted in ascending order. Auto-sort the list.
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

# Returns the maximum number of the passed list of numbers.
def maximum(number_list):
    return max(number_list)

# Returns the minimum number of the passed list of numbers.
def minimum(number_list):
    return min(number_list)

# Returns the POPULATION variance of the passed list of numbers.
def variance(number_list):
    count = count_list(number_list)
    difference = 0
    
    for num in number_list:
        # for each number, substract it by the mean of the list, then square it, and add it to the difference.
        difference = difference + (num - mean(number_list)) ** 2
    
    variance = difference / count

    return variance

# Returns the POPULATION standard deviation of the passed list of numbers.
def standard_deviation(number_list):
    list_variance = variance(number_list)

    # the square root of the variance is the standard deviation.
    standard_deviation = math.sqrt(list_variance)

    return standard_deviation

# Returns the median of the passed list of numbers.
def median(number_list):
    count = count_list(number_list)
    sorted_list = sorted(number_list)

    # get index of middle number.
    middleIndex = math.floor(count / 2)

    # scenario 1: if the count is odd, return the middle-most number.
    if (count % 2) == 1:
        return sorted_list[middleIndex]
    
    # scenario 2: if the count is even, then get the mean of the two middle numbers.
    lower_middle_num = sorted_list[middleIndex - 1]
    upper_middle_num = sorted_list[middleIndex]

    median_of_middle_numbers = mean([lower_middle_num, upper_middle_num])

    return median_of_middle_numbers

##########[ Part 1 Data Loading ]##########

#open csv file
with open('InputDataSample.csv') as csv_file:
    # creating an object of csv reader
    # with the delimiter
    csv_reader = csv.reader(csv_file, delimiter = ',')
 
    # list to store the names of columns
    column = []
 
    # loop to iterate through the rows of csv
    for row in csv_reader:
 
        # adding first row
        column.append(row)
 
        # breaking the loop after the
        # first iteration itself
        break
    # number of columns
    size = int(len(column[0]))
    reader = csv.reader(csv_file)
    # stores each column into array
    columns_as_lists = [list(c) for c in zip(*reader)]
    #for i in range(size):
        # print each column
        #print(columns_as_lists[i])  # All the values in the first column of your CSV
        
# print total number of columns
print("Total columns:", size)
print("List:", columns_as_lists[0])

print("\n\nUnique list:", Unique(columns_as_lists[0]))

