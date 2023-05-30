from solver import Solver
from sorter import Sorter


class CombineSolver(Solver):
    @staticmethod
    def solve(C, w, m, p, T, ab, cd):
        ts, tf = T['start'], T['end']
        n, nw1, nw2 = len(C), 0, 0
        S1, S2, taken_intervals1, taken_intervals2 = [[] for _ in range(m)], [[] for _ in range(m)], \
            [[] for _ in range(m)], [[] for _ in range(m)]
        c1 = C.copy()
        Sorter.bubble_sort_t(c1, ab, cd)
        for i in c1:
            for j in range(m):
                if ab[i]['start'] not in taken_intervals1[j]:
                    S1[j].append(c1[i])
                    nw1 += w[i]
                    taken_intervals1[j].append(ab[i]['start'])
                    break
                elif cd[i]['start'] not in taken_intervals1[j]:
                    S1[j].append(c1[i])
                    nw1 += w[i]
                    taken_intervals1[j].append(cd[i]['start'])
                    break

        c2 = C.copy()
        Sorter.bubble_sort_tw(c2, w, ab, cd)
        for i in c1:
            for j in range(m):
                if ab[i]['start'] not in taken_intervals2[j]:
                    S2[j].append(c1[i])
                    nw2 += w[i]
                    taken_intervals2[j].append(ab[i]['start'])
                elif cd[i]['start'] not in taken_intervals2[j]:
                    S2[j].append(c1[i])
                    nw2 += w[i]
                    taken_intervals2[j].append(cd[i]['start'])

        if nw1 < nw2:
            return S2, nw1
        return S1, nw2
