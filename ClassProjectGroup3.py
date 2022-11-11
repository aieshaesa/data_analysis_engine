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

def count(number_list):
    return len(number_list)

def median(number_list):

    count = len(number_list)

    index = count // 2

    if count % 2:
        return sorted (number_list) [index]

    return sum(sorted(number_list))

def variance(number_list):
    n = len(number_list)
    mean = sum(number_list)

    difference  = [(x - mean) ** 2 for x in data]

    variance = sum(difference) / n

    return variance
