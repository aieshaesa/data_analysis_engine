# course: cmps3500
# CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# FILE: group3tools.py
# DATE: 11/05/2022
# Student 1: Aiesha Esa
# Student 2: Mostafa Abadi
# Student 3: Spencer Denney
# Student 4: Hector Martinez
# description: A Module that contains our own functions for our main project.

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

    for number in list:
        sum = sum + number
        length = length + 1
    
    calculatedMean = sum / length

    return calculatedMean