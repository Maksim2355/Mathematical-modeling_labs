import math
import random as rnd


def reverse_fun(ri, ai, bi):
    return (ri * (bi - ai)) - ai


def rayleigh_distribution(xl, sigma):
    return (xl / sigma ** 2) * math.exp(- ((xl ** 2) / 2 * (sigma ** 2)))


def generate_random_variables(size):
    if size is None:
        return rnd.random()
    r = []
    for i in range(size):
        r.append(rnd.random())
    return r


def fun_gauss(v, m, sigma, N):
    el = math.sqrt(12 / N) * (v - (N / 2))
    return sigma * el + m
