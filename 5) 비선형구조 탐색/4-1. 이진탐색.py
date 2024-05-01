def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid  # 타겟을 찾은 위치(인덱스)를 반환
        if guess > target:
            high = mid - 1  # 중간 값보다 타겟이 작으면, 왼쪽 부분을 탐색
        else:
            low = mid + 1  # 중간 값보다 타겟이 크면, 오른쪽 부분을 탐색

    return -1  # 타겟을 찾지 못한 경우 -1 반환

# 예제 사용
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
target = 9

result = binary_search(arr, target)
print("Target index:", result)
