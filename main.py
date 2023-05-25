from tabulate import tabulate

import experiment_generator
from util import print_results

N = [18, 25, 30, 50, 100]
M = [1, 2, 3, 4, 5]
T_arr = [{'start': 10, 'end': 16},
         {'start': 10, 'end': 17},
         {'start': 10, 'end': 18},
         {'start': 9, 'end': 18},
         {'start': 9, 'end': 19}]

dT, dZ = experiment_generator.with_n(N=N, m=2, T=T_arr[0])
print_results(N, dT, dZ, 'N')
dT, dZ = experiment_generator.with_m(n=50, M=M, T=T_arr[0])
dT, dZ = experiment_generator.with_T(n=50, m=2, T=T_arr)

