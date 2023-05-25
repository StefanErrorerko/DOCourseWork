from combine_solver import CombineSolver
from decompose_solver import DecomposeSolver
from problem_generator import ProblemGenerator
import time


class ProblemSolver:
    def __init__(self, test_amount=10):
        self.TEST_AMOUNT = test_amount

    def test_with_n(self, N, m, T):
        dT, dZ = [], []
        for n in N:
            dt, dz = self.test(n, m, T)
            dT.append(dt)
            dZ.append(dz)
        return dT, dZ

    def test_with_m(self, n, M, T):
        dT, dZ = [], []
        for m in M:
            dt, dz = self.test(n, m, T)
            dT.append(dt)
            dZ.append(dz)
        return dT, dZ

    def test_with_T(self, n, m, T):
        dT, dZ = [], []
        for t in T:
            dt, dz = self.test(n, m, t)
            dT.append(dt)
            dZ.append(dz)
        return dT, dZ

    def test(self, n, m, T):
        dz1, dz2, dz3 = [], [], []
        for _ in range(self.TEST_AMOUNT):
            C, p, w, ab, cd = ProblemGenerator.generate_problem(n, T)
            S, z, t = self.solve_problem(C, w, m, p, T, ab, cd)
            # z_mean = (z[0] + z[1] + z[2]) / 3
            z_mean = (z[0] + z[1]) / 2
            dz1.append((z[0] - z_mean) / z_mean)
            dz2.append((z[1] - z_mean) / z_mean)
            # dz3.append((z3 - z_mean) / z_mean)
        # t1, t2, t3 = sum(t1)/len(t1), sum(t2)/len(t2), sum(t3)/len(t3)
        t1, t2, t3 = sum(t[0]) / len(t[0]), sum(t[1]) / len(t[1]), 0
        # dz1, dz2, dz3 = sum(dz1)/len(dz1), sum(dz2)/len(dz2), sum(dz3)/len(dz3)
        dz1, dz2, dz3 = sum(dz1) / len(dz1), sum(dz2)/len(dz2), 0
        return [t1, t2, t3], [dz1, dz2, dz3]

    def solve_problem(self, C, w, m, p, T, ab, cd):
        t1, t2, t3 = [], [], []
        S = []
        # solving with 1 algorythm, computing time t1 and z1
        start_time = time.time()
        S1, z1 = DecomposeSolver.solve(C, w, m, p, T, ab, cd)
        end_time = time.time()
        t1.append(end_time - start_time)
        S.append(S1)

        # solving with 2 algorythm, computing time t2 and z2
        start_time = time.time()
        S2, z2 = CombineSolver.solve(C, w, m, p, T, ab, cd)
        end_time = time.time()
        t2.append(end_time - start_time)
        S.append(S2)

        # solving with 3 algorythm, computing time t3 and z3
        # place for same stuff for 2 algo

        return S, [z1, z2], [t1, t2, t3]
