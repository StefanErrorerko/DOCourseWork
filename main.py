from tabulate import tabulate

from problem_solver import ProblemSolver
from util import Utility

N = [18, 25, 30, 50, 100]
M = [1, 2, 3, 4, 5]
T_arr = [{'start': 10, 'end': 16},
         {'start': 10, 'end': 17},
         {'start': 10, 'end': 18},
         {'start': 9, 'end': 18},
         {'start': 9, 'end': 19}]

problem_solver = ProblemSolver(10)

dT, dZ = problem_solver.test_with_n(N=N, m=2, T=T_arr[0])
Utility.print_results(N, dT, dZ, 'n')
dT, dZ = problem_solver.test_with_m(n=50, M=M, T=T_arr[0])
Utility.print_results(M, dT, dZ, 'm')
dT, dZ = problem_solver.test_with_T(n=50, m=2, T=T_arr)
Utility.print_results(T_arr, dT, dZ, 'T')


