def solve(C, w, m, p, T, ab, cd):
    ts, tf = T['start'], T['end']
    n, nw, S = len(C), 0, [[]] * m
    servable_clients = C.copy()
    for t in range(ts, tf-1):
        c = []
        for j in range(n):
            if belongs(T, ab[j]) or belongs(T, cd[j]):
                c.append(j)
        bubble_sort_wt(c, w, ab, cd)
        for k in range(m):
            if k < len(c):
                S[k].append(c[k])
                nw += w[k]
                servable_clients.remove(c[k])
    return S, nw


# whether subset belongs to a set
def belongs(subset, set):
    if subset['start'] >= set['start'] and subset['end'] <= set['end']:
        return True
    return False


def interval_len(interval):
    return interval['end'] - interval['start']


def bubble_sort_wt(arr, w, ab, cd):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            t1_1, t2_1 = interval_len(ab[j]), interval_len(cd[j])
            t1_2, t2_2 = interval_len(ab[j+1]), interval_len(cd[j+1])
            if w[j]/(t1_1 + t2_1) < w[j+1]/(t1_2 + t2_2):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
