import math

def fibonacci(n):
    seq = ((((1+math.sqrt(5))/2)**n-((1-math.sqrt(5))/2)**n)/math.sqrt(5))
    return(seq)

def lucas(n):
    seq = (((1+math.sqrt(5))/2)**n+((1-math.sqrt(5))/2)**n)
    return (seq)