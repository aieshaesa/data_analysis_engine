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

import csv

##########[ Part 3 Functions]##########

def mean(number_list):
    listSum = sum(number_list)
    length = len(number_list)

    return listSum / length

# Returns the mode of a list. It reads a sorted (ascending) list of numbers to get its mode.
# it will record a total of same numbers iterated over in the list, until it hits a new number,
# where the total resets to 1 again. The last number that has more occurrences of itself is returned.
def mode(number_list):
    sortedList = sorted(number_list) # list must be sorted in ascending order. Auto-sort the list.
    lastNum = sortedList[0]
    lastNumOccurrences = 0
    currentNumOccurrences = 0

    mode = sortedList[0]

    for num in sortedList:
        if lastNum == num:
            # increment this number's occurence as long as we keep iterating over the same number
            currentNumOccurrences += 1
        
        # if this number's occurrences passes the previous number's occurrences, make this number the new mode.
        if currentNumOccurrences > lastNumOccurrences:            
            mode = lastNum
            lastNumOccurrences = currentNumOccurrences

        # if this current number we are reading isn't the same as the last number iterated, 
        # reset the occurrences value for this new number.
        if lastNum != num:
            currentNumOccurrences = 1
        
        # set the previous iterated item to this (current) one.
        lastNum = num

    return mode

def maximum(number_list):
    return max(number_list)

def minimum(number_list):
    return min(number_list)

def variance(number_list):
    count = len(number_list)
    difference = 0
    
    for num in number_list:
        difference = difference + (num - mean(number_list)) ** 2
    
    variance = difference / n

    return variance

def standard_deviation(number_list):
    count = len(number_list)
    var = variance(numbers_list)
    standardDeviation = math.sqrt(var)

    return standardDeviation

##########[ Part 1 Data Loading]##########

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
    for i in range(size):
        # print each column
        print(columns_as_lists[i])  # All the values in the first column of your CSV
        
# print total number of columns
print("Total columns:", size)