import math

def signum(x):
    """
    Works out if the number is positive,
    negative or zero

    Parameters:
    ----------------
        x : integer
            user input

    Returns:
    -------------
    constants
        -1, 0, 1

    """
    if x > 0:
        return 1
    elif x == 0:
        return 0
    elif x < 0:
        return -1

def min_max(xs):
    """
    Calculates the highest and lowest value of
    the list

    Parameters:
    ----------------
        xs : list 
            list of numbers given by user

    Returns:
    --------------
    float
        first and last values of the list
            

    """
    xs.sort()
    return (xs[0], xs[len(xs) - 1])

def geometric_mean(xs):
    """
    
    Calculates the geometric mean of a list
    of numbers

    Parameters:
    ---------------
        xs : list 
            list of numbers given by user
        total : float
            the result of the multiplication of the numbers
            in the list
        i : integers
            the incrementing value of the for loop

    Returns:
    ----------------
    Float
        Geometric mean on the list

    """
    total = 1
    for i in range(len(xs)):
        total = total * xs[i]
    return total**(1/len(xs))

def swing_time(L):
    """
    
    Computes the time taken for an oscillation of
    an idealised pendulum

    Returns:
    float
        oscillation time

    """
    return (2 * math.pi * math.sqrt(L / 9.81))

def range_squared(n):
    """
    
    Outputs a number of squared values

    Parametres:
    --------------------
        a : list
            outputted list of squared numbers
        i : integer
            loop counter
        n : list
            inputted list of numbers
            
    Returns:
    -----------------
        a : list

    """
    a = []
    for i in range(n):
        a.append(str(i * i))
    return (a)

def count(element, seq):
    """
    
    Counts the instances of the string
    in the list

    Parameters:
    ----------------
        element : string
            is the string who's presence is checked in the sequence
        seq : list
            list of strings
        counter : integer
            counts the instances of the string element

    Returns:
        counter : integer

    """
    counter = 0
    for i in range(len(seq)):
        if element == seq[i]:
            counter = counter + 1
    return(str(counter) + " times")