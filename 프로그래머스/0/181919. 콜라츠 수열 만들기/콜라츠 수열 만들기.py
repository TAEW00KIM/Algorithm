def solution(n):
    arr = [n]
    while n != 1:
        if n % 2 == 0:
            arr.append(n / 2)
            n = n // 2
        else:
            arr.append(3 * n + 1)
            n = 3 * n + 1
    return arr