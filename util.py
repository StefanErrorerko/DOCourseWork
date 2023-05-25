import numpy as np


def rand_normal(mean, start, end):
    scale = 0.25
    rand = int(round(
        (end - start) * np.clip(np.random.normal(loc=mean, scale=scale), 0, 1)))
    return start + rand

def rand_exp(l, start, end):
    rand = int(round(
        (end - start) * np.clip(1/np.random.exponential(1/l), 0, 1)))
    return start + rand
