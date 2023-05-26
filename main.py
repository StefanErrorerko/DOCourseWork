from console_ui import ConsoleUI

N = [18, 25, 30, 50, 100]
M = [1, 2, 3, 4, 5]
T_arr = [{'start': 10, 'end': 16},
         {'start': 10, 'end': 17},
         {'start': 10, 'end': 18},
         {'start': 9, 'end': 18},
         {'start': 9, 'end': 19}]

ui = ConsoleUI(N, M, T_arr)
ui.start()

