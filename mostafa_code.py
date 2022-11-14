#import math

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
    if (count % 2) == 0:
        return sorted_list[middleIndex]
    
    # scenario 2: if the count is even, then get the mean of the two middle numbers.
    lower_middle_num = sorted_list[middleIndex - 1]
    upper_middle_num = sorted_list[middleIndex]

    median_of_middle_numbers = mean([lower_middle_num, upper_middle_num])

    return median_of_middle_numbers

# Returns a value from the sorted number list at the 20th percentile.
# The list is auto-sorted.
# List count must be at least 2.
def percentile_20(number_list):
    count = len(number_list)
    sorted_list = sorted(number_list)
    
    # calculate the percentile, as the 'rank'.
    rank = (0.20 * (count - 1)) + 1
    
    # if rank is an integer, then use the rank as an index and get the value at that index.
    if rank.is_integer():
        return sorted_list[math.floor(rank) - 1]
    else:
        # if rank is a float, then get the value at that index as a integer, then add the rank's fracitional part to its whole part,
        # as the percentile.
        rankIntAndFractional = divmod(rank, 1)
        return rankIntAndFractional[0] + rankIntAndFractional[1]