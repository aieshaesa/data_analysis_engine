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