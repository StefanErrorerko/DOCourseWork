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
        с1 = Sorter.bubble_sort_w(c1, w)
        for i in c1:
            for j in range(m):
                if ab[c1[i]]['start'] not in taken_intervals1[j]:
                    S[j].append(c1[i])
                    nw1 += w[c1[i]]
                    taken_intervals1[j].append(ab[c1[i]]['start'])
                    break
                elif cd[c1[i]]['start'] not in taken_intervals1[j]:
                    S[j].append(c1[i])
                    nw1 += w[c1[i]]
                    taken_intervals1[j].append(cd[c1[i]]['start'])
                    break
        return S, nw1
