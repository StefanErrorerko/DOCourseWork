from solver import Solver
from sorter import Sorter


class GreedySolver(Solver):
    @staticmethod
    def solve(C, w, m, p, T, ab, cd):
        ts, tf = T['start'], T['end']
        n, nw1, nw2 = len(C), 0, 0
        S, taken_intervals1, taken_intervals2 = [[] for _ in range(m)], [[] for _ in range(m)], \
            [[] for _ in range(m)]
        c1 = C.copy()
        Sorter.bubble_sort_w(c1, ab, cd)
        for i in c1:
            for j in range(m):
                if ab[i]['start'] not in taken_intervals1[j]:
                    S[j].append(c1[i])
                    nw1 += w[i]
                    taken_intervals1[j].append(ab[i]['start'])
                    break
                elif cd[i]['start'] not in taken_intervals1[j]:
                    S[j].append(c1[i])
                    nw1 += w[i]
                    taken_intervals1[j].append(cd[i]['start'])
                    break
        return S, nw1
