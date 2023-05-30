from console_ui import ConsoleUI

N = [75, 90, 100, 125, 150]
M = [2, 5, 7, 10, 12]
T_arr = [{'start': 10, 'end': 16},
         {'start': 10, 'end': 17},
         {'start': 10, 'end': 18},
         {'start': 9, 'end': 18},
         {'start': 9, 'end': 19}]

ui = ConsoleUI(N, M, T_arr)
ui.start()

