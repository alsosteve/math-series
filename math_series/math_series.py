import math

def fibonacci(n):
    seq = ((((1+math.sqrt(5))/2)**n-((1-math.sqrt(5))/2)**n)/math.sqrt(5))
    return(seq)

def lucas(n):
    seq = (((1+math.sqrt(5))/2)**n+((1-math.sqrt(5))/2)**n)
    return (seq)

def sum_series(n, first = 0, second = 1):
    if n == 0:
        return first
    if n == 1:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series(n-2, first, second)