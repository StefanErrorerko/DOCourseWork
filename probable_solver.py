from solver import Solver
from sorter import Sorter
from util import Utility


class ProbableSolver(Solver):
    @staticmethod
    def solve(c, w, m, p, T, ab, cd):
        nw = 0
        for k in range(1, 101):
            s_local = [[] for _ in range(m)]
            nw_Local = 0
            taken_interv = [[] for _ in range(m)]
            C = c.copy()

            Sorter.bubble_sort_tw(C, w, ab, cd)
            for i in range(0, len(C)):
                for j in range(0, m):
                    ab_free = ProbableSolver.find_free_intervals(taken_interv[j], ab[C[i]]['start'], ab[C[i]]['end'])
                    cd_free = ProbableSolver.find_free_intervals(taken_interv[j], cd[C[i]]['start'], cd[C[i]]['end'])
                    all_free = ab_free + cd_free
                    if len(all_free) > 0:
                        random_index = Utility.rand_normal(0.5, 0, len(all_free) - 1)
                        random_interval = all_free[random_index]
                        taken_interv[j].append(random_interval)
                        s_local[j].append(C[i])
                        nw_Local += w[C[i]]
                        break

            if nw_Local > nw:
                S = s_local
                nw = nw_Local
        return S, nw

    @staticmethod
    def find_free_intervals(schedule, start, end):
        intervals = []
        # define all intervals when client is able to be served
        for i in range(end - start):
            intervals.append([start + i, start + i + 1])
        for j in range(len(schedule)):
            if schedule[j] in intervals:
                intervals.remove(schedule[j])
        return intervals

        '''
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
        '''