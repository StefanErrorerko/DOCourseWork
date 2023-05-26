# -*- coding: utf-8 -*-
from controller import Controller
from tabulate import tabulate


class ConsoleUI:
    def __init__(self, N, M, T_arr, n=50, m=2):
        self.N = N
        self.M = M
        self.T_arr = T_arr
        self.n = n
        self.m = m
        self.T = T_arr[0]

    def start(self):
        self.display_start_menu()
    def display_start_menu(self):
        print("Для початку оберіть режим роботи:")
        print("1. Розв'язати алгоритм доступним алгоритмом\n"
              "2. Провести експеримент зі зміною кількості клієнтів n\n"
              "3. Провести експеримент зі зміною кількості бригад m\n"
              "4. Провести експеримент зі зміною інтервалу роботи [Ts; Tf]\n"
              "5. Завершити роботу програми")
        self.get_start_choice()

    def get_start_choice(self):
        key = input("Введіть номер режиму: ")

        cases = {
            '1': lambda: self.display_solving(),
            '2': lambda: self.display_test_with_n(),
            '3': lambda: self.display_test_with_m(),
            '4': lambda: self.display_test_with_T(),
            '5': lambda: Controller.exit()
        }

        cases.get(key, lambda: (
            print("Ви ввели невірне значення"),
            self.get_start_choice()
        ))()
    def display_solving(self):
        print("Для початку оберіть режим отримання значень:")
        print("1. Ввід з консолі"
              "2. Випадковим чином"
              "3. Зчитування з файлу")
        self.get_value_input_option()

    def get_value_input_option(self):
        key = input("Введіть номер режиму: ")
        cases = {
            '1': lambda: self.solve_value_from_console(),
            '2': lambda: self.solve_value_from_random(),
            '3': lambda: self.solve_value_from_file()
        }

        cases.get(key, lambda: (
            print("Ви ввели невірне значення"),
            self.get_value_input_option()
        ))()

    def display_test_with_n(self):
        dT, dZ = Controller.test_with_n(N=self.N, m=self.m, T=self.T)
        self.print_test_results(self.N, dT, dZ, 'n')

    def display_test_with_m(self):
        dT, dZ = Controller.test_with_m(n=self.n, M=self.M, T=self.T)
        self.print_test_results(self.M, dT, dZ, 'm')

    def display_test_with_T(self):
        dT, dZ = Controller.test_with_T(n=self.n, m=self.m, T=self.T_arr)
        self.print_test_results(self.T_arr, dT, dZ, 'T')

    def solve_value_from_console(self):
        try:
            w, ab, cd = [], [], []
            n = int(input("Введіть кількість клієнтів: "))
            m = int(input("Введіть кількість бригад: "))
            Ts, Tf = input("Введіть інтервал роботи бригад (через кому у год): ").split(", ")
            T = {'start': int(Ts), 'end': int(Tf)}
            for i in range(n):
                w_i = int(input(f"Введіть вагу клієнта (від 1 до 3): "))
                w.append(w_i)
                a, b, c, d = input(f"Введіть проміжки, в яких вільний клієнт №{i+1} (через кому у год): ").split(", ")
                ab.append({'start': int(a), 'end': int(b)})
                cd.append({'start': int(c), 'end': int(d)})
                Controller.check_values(n, w_i, m, T, ab, cd)
        except:
            print("Введено невірні дані")
            self.solve_value_from_console()
        self.get_solving_option(n, w, m, 1, T, ab, cd)

    def solve_value_from_random(self):
        C, w, m, p, T, ab, cd = Controller.get_random_parameters()
        self.get_solving_option(len(C), w, m, p, T, ab, cd)

    def solve_value_from_file(self):
        n, w, m, p, T, ab, cd = Controller.load_parameters()
        self.get_solving_option(n, w, m, p, T, ab, cd)

    def get_solving_option(self, n, w, m, p, T, ab, cd):
        print("Оберіть один із доступних алгоритмів для розв'язання")
        print("1. Розв'язати задачу алгоритмом розкладу з декомпозицією\n"
              "2. Розв'язати задачу комбінованим жадібним алгоритмом\n"
              "3. Розв'язати задачу ймовірнісним алгоритмом\n")
        self.get_solving_choice(n, w, m, p, T, ab, cd)

    def get_solving_choice(self, n, w, m, p, T, ab, cd):
        key = input("Введіть номер алгоритму: ")
        cases = {
            '1': lambda: self.display_decompose_solving(n, w, m, p, T, ab, cd),
            '2': lambda: self.display_combine_solving(n, w, m, p, T, ab, cd),
            '3': lambda: self.display_probable_solving(n, w, m, p, T, ab, cd)
        }

        cases.get(key, lambda: (
            print("Ви ввели невірне значення"),
            self.get_solving_choice(n, w, m, p, T, ab, cd)
        ))()

    def display_decompose_solving(self, n, w, m, p, T, ab, cd):
        C = []
        for i in range(n):
            C.append(i)
        S, nw = Controller.decompose_solve(C, w, m, p, T, ab, cd)
        print("Результат роботи алгоритму розкладу з декомпозицією:")
        self.print_solve_results(S, nw)

    def display_combine_solving(self, n, w, m, p, T, ab, cd):
        C = []
        for i in range(n):
            C.append(i)
        S, nw = Controller.combine_solve(C, w, m, p, T, ab, cd)
        print("Результат роботи комбінованого жадібного алгоритму:")
        self.print_solve_results(S, nw)

    def display_probable_solving(self, n, w, m, p, T, ab, cd):
        C = []
        for i in range(n):
            C.append(i)
        S, nw = Controller.probable_solve(C, w, m, p, T, ab, cd)
        print("Результат роботи ймовірнісного алгоритму:")
        self.print_solve_results(S, nw)

    def print_solve_results(self, S, nw):
        print(f"Розклад: {S}")
        print(f"ЦФ: {nw}")

    def print_test_results(self, observable_values, dT, dZ, nameof_value):
        header_column = [nameof_value,
                         'dT Algo 1', 'dT Algo 2', 'dT Algo 3',
                         'dZ Algo 1', 'dZ Algo 2', 'dZ Algo 3']
        dT = self.reshape(dT, 3, len(dT))
        dZ = self.reshape(dZ, 3, len(dZ))

        table_data = list(zip(observable_values,
                              dT[0], dT[1], dT[2],
                              dZ[0], dZ[1], dZ[2]))
        table = tabulate(table_data, headers=header_column, tablefmt="grid")
        print(table)

    def reshape(self, arr, r, c):
        new_arr = []
        for i in range(r):
            new_arr.append([])
            for j in range(c):
                new_arr[i].append(arr[j][i])
        return new_arr









