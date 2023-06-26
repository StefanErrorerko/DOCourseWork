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
                if ab[c1[i]]['start'] not in taken_intervals1[j]:
                    S1[j].append(c1[i])
                    nw1 += w[c1[i]]
                    taken_intervals1[j].append(ab[c1[i]]['start'])
                    break
                elif cd[c1[i]]['start'] not in taken_intervals1[j]:
                    S1[j].append(c1[i])
                    nw1 += w[c1[i]]
                    taken_intervals1[j].append(cd[c1[i]]['start'])
                    break

        c2 = C.copy()
        Sorter.bubble_sort_tw(c2, w, ab, cd)
        for i in c1:
            for j in range(m):
                if ab[c2[i]]['start'] not in taken_intervals2[j]:
                    S2[j].append(c2[i])
                    nw2 += w[c2[i]]
                    taken_intervals2[j].append(ab[c2[i]]['start'])
                    break
                elif cd[c2[i]]['start'] not in taken_intervals2[j]:
                    S2[j].append(c2[i])
                    nw2 += w[c2[i]]
                    taken_intervals2[j].append(cd[c2[i]]['start'])
                    break
        if nw1 < nw2:
            return S2, nw2
        return S1, nw1
