import decompose_solver
import problem_generator
import time

TEST_AMOUNT = 10


def with_n(N, m, T):
    dT, dZ = [], []
    for n in N:
        dt, dz = test_problem(n, m, T)
        dT.append(dt)
        dZ.append(dz)
    return dT, dZ


def with_m(n, M, T):
    dT, dZ = [], []
    for m in M:
        dt, dz = test_problem(n, m, T)
        dT.append(dt)
        dZ.append(dz)
    return dT, dZ


def with_T(n, m, T):
    dT, dZ = [], []
    for t in T:
        dt, dz = test_problem(n, m, t)
        dT.append(dt)
        dZ.append(dz)
    return dT, dZ


def test_problem(n, m, T):
    t1, t2, t3, dz1, dz2, dz3 = [], [], [], [], [], []
    for _ in range(TEST_AMOUNT):
        C, p, w, ab, cd = problem_generator.generate_problem(n, T)

        # solving with 1 algorythm, computing time t1 and z1
        start_time = time.time()
        S, z1 = decompose_solver.solve(C, w, m, p, T, ab, cd)
        end_time = time.time()
        t1.append(end_time - start_time)

        # solving with 2 algorythm, computing time t2 and z2
        # place for same stuff for 2 algo

        # solving with 3 algorythm, computing time t3 and z3
        # place for same stuff for 2 algo

        #z_mean = (z1 + z2 + z3) / 3
        z_mean = z1
        dz1.append((z1 - z_mean) / z_mean)
        #dz2.append((z2 - z_mean) / z_mean)
        #dz3.append((z3 - z_mean) / z_mean)
    # t1, t2, t3 = sum(t1)/len(t1), sum(t2)/len(t2), sum(t3)/len(t3)
    t1, t2, t3 = sum(t1) / len(t1), 0, 0
    # dz1, dz2, dz3 = sum(dz1)/len(dz1), sum(dz2)/len(dz2), sum(dz3)/len(dz3)
    dz1, dz2, dz3 = sum(dz1) / len(dz1), 0, 0
    return [t1, t2, t3], [dz1, dz2, dz3]







