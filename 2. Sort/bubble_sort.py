# sort function;
from Note.calculate_time import calculate_time
import random


def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - 1 - i):
            if li[j] > li[j + 1]:
                li[j + 1], li[j] = li[j], li[j + 1]


li = [random.randint(0, 100) for i in range(10)]
print(li)
bubble_sort(li)
print(li)

