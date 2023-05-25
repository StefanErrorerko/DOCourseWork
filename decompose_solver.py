import numpy as np
from solver import Solver
from util import Utility
from sorter import Sorter


class DecomposeSolver(Solver):
    @staticmethod
    def solve(C, w, m, p, T, ab, cd):
        ts, tf = T['start'], T['end']
        n, nw, S = len(C), 0, [[] for _ in range(m)]
        servable_clients = C.copy()
        for t in range(ts, tf-1):
            c = []
            t = {'start': t, 'end': t + 1}
            for j in range(len(servable_clients)):
                if Utility.belongs(t, ab[j]) or Utility.belongs(t, cd[j]):
                    c.append(servable_clients[j])
            Sorter.bubble_sort_wt(c, w, ab, cd)
            for k in range(m):
                if k < len(c):
                    S[k].append(c[k])
                    nw += w[k]
                    servable_clients.remove(c[k])
        return S, nw

