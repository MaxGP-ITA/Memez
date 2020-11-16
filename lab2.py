"""Imports the math functions"""
import math

def box_volume(length1, length2, length3):
    """The function takes 3 numbers, either integers or floats and multiplies them together
    to give the volume of a cuboid"""
    return (length1 * length2 * length3)

def fall_time(height):
    """The function takes a number either a float or an integer and multiplies it with the
    half the value of g to give the time of a fall from a given height on Earth"""
    return (0.5 * 9.81 * height)

def interval_point(Start, End, Fraction):
    """The function takes 3 numbers, either integers or floats and with an if statement
    verifies if the value of fraction is between 1 and 0"""
    if Fraction > 1 & Fraction < 0:
        print('Fractional Value must be between 0 and 1')
    else:        
        """If the value of fraction is accepted, the function returns a fraction of the 
        difference between the value of Start and End and adds it to start"""
        return Fraction * math.absolute(End - Start) + Start
    
def impact_velocity(height):
    """The function takes a number, and calls the function fall_time. It then multiplies 
    this value by g to give the velocity on impact of an object dropped at that height"""
    fall_time(height)
    return (height * 9.81)

def seconds2days(seconds):
    """There are 86400 in a day, therefore this division gives the number of days in the
    given seconds"""
    return (86400 / seconds)

def box_surface(length, height, width):
    """I just copied the formula  from the lab to be honest"""
    s = (length + height + width) / 2    
    return math.sqrt(s(s-length)(s - height)(s - width))