import decompose_solver
import problem_generator

n, m, T = 18, 2, {'start': 10, 'end': 16}

C, p, w, ab, cd = problem_generator.generate_problem(n, T)
S, z1 = decompose_solver.solve(C, w, m, p, T, ab, cd)
print(S)
print(z1)