import random
from util import Utility


class ProblemGenerator:
    @staticmethod
    def generate_problem(n, T):
        C, w, ab, cd = [], [], [], []
        ts, tf = T['start'], T['end']
        p = 1
        for i in range(n):
            C.append(i)
            w_i = Utility.rand_exp(0.25, 1, 3)
            w.append(w_i)
            t1 = Utility.rand_normal(0.3/w_i, p, tf-ts-p)
            t2 = Utility.rand_normal(0.3/w_i, p, tf-ts-t1)
            a = random.randint(ts, tf-t2-t1)
            b = a + t1
            c = random.randint(b, tf-t2)
            d = c + t2
            ab.append({'start': a, 'end': b})
            cd.append({'start': c, 'end': d})
        return C, p, w, ab, cd
