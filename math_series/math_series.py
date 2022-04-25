import math

def fibonacci(n):
    ''' Function returns nth
    value in the fibonacci
    series.One parameter n -> number.\
        Returns number
    '''
    seq = ((((1+math.sqrt(5))/2)**n-((1-math.sqrt(5))/2)**n)/math.sqrt(5))
    return(seq)

def lucas(n):
    '''
    Function returns the nth value in the lucas numbers.
    '''
    seq = (((1+math.sqrt(5))/2)**n+((1-math.sqrt(5))/2)**n)
    return (seq)

def sum_series(n, first = 0, second = 1):
    '''
    his function with no optional parameters will produce numbers from the fibonacci series.
    Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers.
    '''
    if n == 0:
        return first
    if n == 1:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series(n-2, first, second)