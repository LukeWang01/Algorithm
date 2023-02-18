def count_sort(lst, max_count=100):
    count = [0 for _ in range(max_count + 1)]
    for val in lst:
        count[val] += 1
    lst.clear()

    for idx, val in enumerate(count):
        # print(idx, val)
        for i in range(val):
            lst.append(idx)


import random

lst = [random.randint(0, 100) for _ in range(1000)]

# print(lst)
count_sort(lst)
# print(lst)
