class ConsoleUI:
    @staticmethod
    def start():
        ConsoleUI.display_start_menu()
    @staticmethod
    def display_start_menu():
        print("Для початку оберіть режим роботи:")
        print("1. Розв'язати задачу алгоритмом розкладу з декомпозицією"
              "2. Розв'язати задачу комбінованим жадібним алгоритмом"
              "3. Розв'язати задачу ймовірнісним алгоритмом"
              "4. Провести експеримент зі зміною кількості клієнтів n"
              "5. Провести експеримент зі зміною кількості бригад m"
              "6. Провести експеримент зі зміною інтервалу роботи [Ts; Tf]"
              "7. Завершити роботу програми")

        def display_start_choice():
            key = input("Введіть номер режиму: ")
            cases = {
                '1': lambda: print("Case 'a' executed."),
                '2': lambda: print("Case 'b' executed."),
                '3': lambda: print("Case 'c' executed."),
                '4': lambda: print("Case 'c' executed."),
                '5': lambda: print("Case 'c' executed."),
                '6': lambda: print("Case 'c' executed."),
                '7': lambda: print("Case 'c' executed."),
            }

            cases.get(key, lambda: (
                print("ви ввели невірне значення"),
                display_start_choice()
            ))()