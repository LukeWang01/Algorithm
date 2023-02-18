def bucket_sort(lst, n=100, max_num=10000):
    # 100 bucket,
    buckets = [[] for _ in range(n)]  # create bucket

    for var in lst:
        i = min(var // (max_num//n), n - 1)  # bucket number

        buckets[i].append(var)  # add to bucket

        # maintain order within bucket
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break

    res = []

    for bucket in buckets:
        res.extend(bucket)
    return res