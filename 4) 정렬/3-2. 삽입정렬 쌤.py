def insertion(li):
    n = len(li)
    for i in range(1, n):
        key = li[i]
        j = i - 1
        while j >= 0 and li[j] > key:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = key
        print(i,li)

li=[1,2,5,7,3,4,8,9]
insertion(li)
