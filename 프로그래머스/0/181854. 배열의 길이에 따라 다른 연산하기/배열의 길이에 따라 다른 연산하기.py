def solution(arr, n):
    for idx, i in enumerate(arr):
        if len(arr) % 2 == 1:
            if idx % 2 == 0:
                arr[idx] += n
        else:
            if idx % 2 == 1:
                arr[idx] += n
    return arr