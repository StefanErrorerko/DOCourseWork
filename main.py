from console_ui import ConsoleUI

N_prompts = 100
N = [10, 15, 20, 25, 50]
M = [2, 3, 4, 5, 6]
T_arr = [{'start': 10, 'end': 16},
         {'start': 10, 'end': 17},
         {'start': 10, 'end': 18},
         {'start': 9, 'end': 18},
         {'start': 9, 'end': 19}]

ui = ConsoleUI(N, M, T_arr, N_prompts)
ui.start()

