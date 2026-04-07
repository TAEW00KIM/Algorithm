def solution(numbers, n):
    total = 0
    for i in numbers:
        if total > n:
            break
        total += i
    return total