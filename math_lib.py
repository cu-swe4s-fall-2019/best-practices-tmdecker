import math


def mean(V):
    return sum(V) / len(V)


def stdev(V):
    return math.sqrt(sum([(mean(V)-x)**2 for x in V]) / len(V))