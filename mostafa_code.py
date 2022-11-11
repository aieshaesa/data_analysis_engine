import math

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

def median(number_list):
    count = len(number_list)

    # divide count by 2 then round the result down.
    index = count // 2

    sorted_list = sorted(number_list)

    # if list count is divisible by 2
    if count % 2:
        return sorted_list[index]
    
    return sum(sorted_list)