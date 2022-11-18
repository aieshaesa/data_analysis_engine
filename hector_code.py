# my part 3 functions that I wrote

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


MONTH_COL = 0
DAY_OF_WEEK_COL = 1
NUMBER_OF_SEATS_COL = 7

columns = [ [1, 3, 8], [6, 0, 5], ... ]

month_column = columns[MONTH_COL]
day_of_week_column = columns[DAY_OF_WEEK_COL]
