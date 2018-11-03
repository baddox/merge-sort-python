import random
import math


class MergeSort:
    def __init__(self, splitter=2):
        self.splitter = splitter
        # self.sort_calls = 0
        # self.merge_calls = 0
        self.comparisons = 0

    def merge(self, a, b):
        a, b = list(a), list(b)
        merged = []
        smaller, bigger = a, b
        while smaller and bigger:
            self.comparisons += 1
            if smaller[0] <= bigger[0]:
                merged.append(smaller.pop(0))
            else:
                smaller, bigger = bigger, smaller
        # Now either smaller or bigger (but not both) may have some remaining
        # items, so just append them both.
        merged = merged + smaller + bigger
        return merged

    def merge2(self, a, b):
        a_length, b_length = len(a), len(b)
        a_index, b_index = 0, 0
        merged = []
        while a_index < a_length and b_index < b_length:
            self.comparisons += 1
            if a[a_index] <= b[b_index]:
                merged.append(a[a_index])
                a_index += 1
            else:
                merged.append(b[b_index])
                b_index += 1
        if a_index < a_length:
            merged += a
        if b_index < b_length:
            merged += b
        return merged

    def sort(self, items):
        length = len(items)
        if length == 1 or length == 0:
            return items, self.comparisons
        # debugging
        # global calls
        # global total_length
        # calls += 1
        # total_length += length
        # print("\t".join(map(str, [calls, "merge_sort", length, total_length])))
        # debugging
        if self.splitter == 2:
            half = length // self.splitter
        else:
            half = max(length // self.splitter, 1)
        a, b = items[:half], items[half:]
        sorted_a, _ = self.sort(a)
        sorted_b, _ = self.sort(b)
        return self.merge(sorted_a, sorted_b), self.comparisons


def main():
    # items = list(range(16))
    # random.shuffle(items)
    # # print(items)
    # sorted_items, comparisons = MergeSort().sort(items)
    # # print(sorted_items)

    for i in range(10):
        exp = i + 8
        num = 2 ** exp
        items = list(range(num))
        # random.shuffle(items)
        items = items[::-1]
        sorted_items, comparisons = MergeSort(2).sort(items)
        if sorted_items != sorted(items):
            raise "AHHH"
        runtime = round(math.log(comparisons, 2))
        print("\t".join(map(str, [num, comparisons, exp, runtime])))
        # print()

    # a = []
    # b = []

    # a = [1, 2, 3, 4, 5, 6]
    # b = [7, 8]

    # a = []
    # b = [7, 8, 9]
    # a, b = b, a

    # a = [1, 2, 3, 7, 8, 9, 13, 14, 15]
    # b = [4, 5, 6, 10, 11, 12, 16, 17, 18, 19]

    # print(merge(a, b))


main()
