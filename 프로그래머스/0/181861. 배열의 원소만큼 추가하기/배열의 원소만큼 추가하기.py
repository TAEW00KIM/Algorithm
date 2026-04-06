def solution(arr):
    result = []
    for i in arr:
        result.extend([i] * i)
    return result