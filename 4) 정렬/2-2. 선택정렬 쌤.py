def selection(li):
    n = len(li)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if li[min_idx]>li[j]:
                min_idx=j
        li[i], li[min_idx] = li[min_idx], li[i]
        print(li)    


li = [4, 6, 1, 7, 2, 8, 3, 5, 9, 10, 12, 11]
selection(li)
print(li)