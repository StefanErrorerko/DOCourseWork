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

    @staticmethod
    def print_results(observable_values, dT, dZ, nameof_value):
        header_column = [nameof_value,
                         'dT Algo 1', 'dT Algo 2', 'dT Algo 3',
                         'dZ Algo 1', 'dZ Algo 2', 'dZ Algo 3']
        dT = Utility.reshape(dT, 3, len(dT))
        dZ = Utility.reshape(dZ, 3, len(dZ))

        table_data = list(zip(observable_values,
                              dT[0], dT[1], dT[2],
                              dZ[0], dZ[1], dZ[2]))
        table = tabulate(table_data, headers=header_column, tablefmt="grid")
        print(table)

    @staticmethod
    def reshape(arr, r, c):
        new_arr = []
        for i in range(r):
            new_arr.append([])
            for j in range(c):
                new_arr[i].append(arr[j][i])
        return new_arr
