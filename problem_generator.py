import random
import util


def generate_problem(n, T):
    C, w, ab, cd = [], [], [], []
    ts, tf = T['start'], T['end']
    for i in range(n):
        C.append(i)
        p = 1
        w.append(util.rand_normal(1, 3))
        t1 = util.rand_normal(p, tf-ts-p)
        t2 = util.rand_normal(p, tf-ts-t1)
        a = util.rand_normal(ts, tf-t2-t1)
        b = a + t1
        c = util.rand_normal(b, tf-t2)
        d = c + t2
        ab.append({'start': a, 'end': b})
        cd.append({'start': c, 'end': d})
    return C, p, w, ab, cd
