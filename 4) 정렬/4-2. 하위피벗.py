def quicksorted(arr):
    if len(arr) > 1:
        pivot = arr[len(arr)-1]
        left, mid, right = [], [], []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
            print(left,mid,right)
        mid.append(pivot)
        return quicksorted(left) + mid + quicksorted(right)
    else:
        return arr
        
arr= [5,8,4,2,6,1,3,9,7]
print(quicksorted(arr))