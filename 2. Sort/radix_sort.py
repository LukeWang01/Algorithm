def radix_sort(lst):
    max_num = max(lst)
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for val in lst:
            digit = (val // 10 ** it) % 10
            buckets[digit].append(val)

        lst.claer()

        for bucket in buckets:
            lst.extend(bucket)

        it += 1

        # repeat input and output.