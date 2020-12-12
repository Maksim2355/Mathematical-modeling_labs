import math
import random as rnd


def reverse_fun(ri, ai, bi):
    return (ri * (bi - ai)) - ai


def rayleigh_distribution(xl, sigma):
    return (xl / sigma ** 2) * math.exp(- ((xl ** 2) / 2 * (sigma ** 2)))


def generate_random_variables(size):
    r = []
    for i in range(size):
        r.append(rnd.random())
    return r
