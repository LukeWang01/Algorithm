
def shell_sort_v2(li):
    gap = len(li) // 2
    while gap > 0:
        for i in range(gap, len(li)):
            tmp = li[i]
            j = i - gap
            while j >= 0 and tmp < li[j]:
                li[j + gap] = li[j]
                j -= gap
            li[j + gap] = tmp
        gap //= 2

lst = [2,1,4,6,7,3,5,9,8]
shell_sort_v2(lst)
print(lst)