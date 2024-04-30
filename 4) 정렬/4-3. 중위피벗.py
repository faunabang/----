def quick_sort(a):
    def sort(left, right):
        if right <= left:
            return

        mid = partition(left, right)
        sort(left, mid - 1)
        sort(mid, right)

    def partition(pl, pr):
        pivot = a[(pl + pr)//2]
        print(pl,pr,end='')
        while pl <= pr:
            while a[pl] < pivot:
                pl += 1
            while a[pr] > pivot:
                pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl, pr= pl + 1, pr - 1
        print(a)
        return pl
    
    return sort(0, len(a) - 1)

a=[5,8,4,2,6,1,3,9,7]
quick_sort(a)
