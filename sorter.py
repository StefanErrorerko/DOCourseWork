from util import Utility


class Sorter:
    @staticmethod
    def bubble_sort_wt(arr, w, ab, cd):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                t1_1, t2_1 = Utility.interval_len(ab[j]), Utility.interval_len(cd[j])
                t1_2, t2_2 = Utility.interval_len(ab[j + 1]), Utility.interval_len(cd[j + 1])
                if w[j] / (t1_1 + t2_1) < w[j + 1] / (t1_2 + t2_2):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    @staticmethod
    def bubble_sort_t(arr, ab, cd):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                t1_1, t2_1 = Utility.interval_len(ab[j]), Utility.interval_len(cd[j])
                t1_2, t2_2 = Utility.interval_len(ab[j + 1]), Utility.interval_len(cd[j + 1])
                if (t1_1 + t2_1) > (t1_2 + t2_2):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    @staticmethod
    def bubble_sort_tw(arr, w, ab, cd):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                t1_1, t2_1 = Utility.interval_len(ab[j]), Utility.interval_len(cd[j])
                t1_2, t2_2 = Utility.interval_len(ab[j + 1]), Utility.interval_len(cd[j + 1])
                if (t1_1 + t2_1) / w[j] < (t1_2 + t2_2) / w[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    @staticmethod
    def bubble_sort_w(arr, w, ab, cd):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                t1_1, t2_1 = Utility.interval_len(ab[j]), Utility.interval_len(cd[j])
                t1_2, t2_2 = Utility.interval_len(ab[j + 1]), Utility.interval_len(cd[j + 1])
                if w[j] < w[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]