import numpy as np


def rand_normal(start, end):
    mean = 2
    std_dev = 0.5
    rand = int(round(np.random.normal(loc=mean, scale=std_dev)))
    return np.clip(rand, start, end)