from solver import Solver
from util import Utility


class ProbableSolver(Solver):
    @staticmethod
    def solve(c, w, m, p, T, ab, cd):
        nw = 0
        for k in range(1, 101):
            s_local = [[] for _ in range(m)]
            nw_Local = 0
            taken_interv = [[] for _ in range(m)]

            for i in range(0, len(c)):
                for j in range(0, m):
                    all_free = []
                    ab_free = ProbableSolver.find_free_intervals(taken_interv[j], ab[i]['start'], ab[i]['end'])
                    cd_free = ProbableSolver.find_free_intervals(taken_interv[j], cd[i]['start'], cd[i]['end'])
                    t1 = ab_free[1] - ab_free[0]
                    for t in range(t1):
                        all_free.append(ab_free[0] + t)
                    t2 = cd_free[1]-cd_free[0]
                    for t in range(t2):
                        all_free.append(cd_free[0] + t)
                    if len(all_free) > 0:
                        random_index = Utility.rand_normal(0.5, 0, len(all_free) - 1)
                        random_start = all_free[random_index]
                        taken_interv[j].append(random_start)
                        s_local[j].append(c[i])
                        nw_Local += w[i]
                        break

            if nw_Local > nw:
                S = s_local
                nw = nw_Local
        return S, nw

    @staticmethod
    def find_free_intervals(numbers, a, b):
        if not numbers:
            return [a, b]
        elif len(numbers) == 1:
            num = numbers[0]
            if num < a or num > b:
                return [a, b]

        intervals = []
        numbers.sort()

        if numbers[0] - a >= 1:
            intervals.append(a)
            intervals.append(numbers[0] - 1)

        for i in range(len(numbers) - 1):
            if numbers[i + 1] - numbers[i] >= 2:
                intervals.append(numbers[i] + 1)
                intervals.append(numbers[i + 1] - 1)

        if b - numbers[-1] >= 1:
            intervals.append(numbers[-1] + 1)
            intervals.append(b)

        return intervals