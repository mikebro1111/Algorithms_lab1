import random


def random_sampler(size):
    return [random.randint(-10**9, 10**9) for _ in range(size)]


def random_small_sampler(size):
    return [random.randint(1, 3) for _ in range(size)]


def increasing_sampler(size):
    return list(range(1, size))


def decreasing_sampler(size):
    return increasing_sampler(size)[::-1]
