import numpy as np
from tabulate import tabulate


class Utility:
    @staticmethod
    def rand_normal(mean, start, end):
        scale = 0.25
        rand = int(round(
            (end - start) * np.clip(np.random.normal(loc=mean, scale=scale), 0, 1)))
        return start + rand

    @staticmethod
    def rand_exp(l, start, end):
        rand = int(round(
            (end - start) * np.clip(1/np.random.exponential(1/l), 0, 1)))
        return start + rand

    @staticmethod
    def interval_len(interval):
        return interval['end'] - interval['start']

    # whether subset belongs to a set
    @staticmethod
    def belongs(subset, set):
        if subset['start'] >= set['start'] and subset['end'] <= set['end']:
            return True
        return False
