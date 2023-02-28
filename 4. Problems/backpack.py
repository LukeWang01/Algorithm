goods = [(60, 10), (100, 20), (120, 30)]
goods.sort(key=lambda x:x[0]/x[1], reverse=True)


def greedy_backpack_fractional(goods, w):

    m = [0 for i in range(len(goods))]
    total_v = 0
    for i, (price, weight) in enumerate(goods):
        if weight <= w:
            m[i] = 1
            w -= weight
            total_v += price
        else:
            m[i] = w / weight
            w = 0
            total_v += price * m[i]
            break
    return m, total_v


from functools import cmp_to_key


def xy_cmp(x, y):
    if x+y < y+x:
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0


def number_join(lst):
    li = list(map(str, lst))
    li.sort(key=cmp_to_key(xy_cmp))
    return "".join(li)



def activity_selection(a):
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] >= res[-1][1]:
            res.append(a[i])
        else:
            continue

    return res
