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

def mean(number_list: list) -> float:
    """Computes the mean of a list of numbers.

    Args: 
        number_list: A list containing numbers or floats.
    
    Returns: 
        A float representing the mean.
    """

    sum = 0
    length = 0
    calculatedMean = 0

    for number in number_list:
        sum = sum + number
        length = length + 1
    
    calculatedMean = sum / length

    return calculatedMean