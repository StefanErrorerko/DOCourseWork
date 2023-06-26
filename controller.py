from greedy_solver import GreedySolver
from problem_generator import ProblemGenerator
from problem_solver import ProblemSolver
import json
import sys


class Controller:
    @staticmethod
    def check_values(n, w, m, T, ab, cd):
        if (n < 0 or
                w < 1 or w > 3 or
                m < 0 or
                T['end'] - T['start'] < 1):
            raise Exception("Невірний формат введених даних")
        for i in range(len(ab)):
            if(ab[i]['end'] - ab[i]['start'] < 1 or
                    cd[i]['end'] - cd[i]['start'] < 1):
                raise Exception("Невірний формат введених проміжків")

    @staticmethod
    def decompose_solve(C, w, m, p, T, ab, cd):
        solver = ProblemSolver()
        return solver.decompose_solve(C, w, m, p, T, ab, cd)

    @staticmethod
    def combine_solve(C, w, m, p, T, ab, cd):
        solver = ProblemSolver()
        return solver.combine_solve(C, w, m, p, T, ab, cd)

    @staticmethod
    def probable_solve(C, w, m, p, T, ab, cd, N):
        solver = ProblemSolver()
        return solver.probable_solve(C, w, m, p, T, ab, cd)

    @staticmethod
    def greedy_solve(C, w, m, p, T, ab, cd):
        solver = ProblemSolver()
        return solver.greedy_solve(C, w, m, p, T, ab, cd)

    @staticmethod
    def get_random_parameters():
        n, m, T = ProblemGenerator.generate_parameters()
        C, p, w, ab, cd = ProblemGenerator.generate_problem(n, T)
        return C, w, m, p, T, ab, cd

    @staticmethod
    def load_parameters():
        PATH = "data.json"
        with open(PATH) as file:
            data = json.load(file)
        n = data['n']
        m = data['m']
        w = data['w']
        p = data['p']
        T = data['T']
        T = {'start': T[0], 'end': T[1]}
        ab, cd = [], []
        for i in range(len(data['ab'])):
            ab.append({'start': data['ab'][i][0], 'end': data['ab'][i][1]})
            cd.append({'start': data['cd'][i][0], 'end': data['cd'][i][1]})
        return n, w, m, p, T, ab, cd

    @staticmethod
    def test_with_n(N, m, T):
        problem_solver = ProblemSolver()
        return problem_solver.test_with_n(N, m, T)

    @staticmethod
    def test_with_m(n, M, T):
        problem_solver = ProblemSolver()
        return problem_solver.test_with_m(n, M, T)


    @staticmethod
    def test_with_T(n, m, T):
        problem_solver = ProblemSolver()
        return problem_solver.test_with_T(n, m, T)

    @staticmethod
    def exit():
        sys.exit()
