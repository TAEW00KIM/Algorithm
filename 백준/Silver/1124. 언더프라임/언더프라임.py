import math
import sys
input = sys.stdin.readline

def solution(n):
    arr = []
    x = 2
    while n > 1:
        if n % x == 0:
            arr.append(x)
            n = n // x
        else:
            x += 1
            if x > int(math.sqrt(n)): x = n
    return arr

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

a, b = map(int, input().split())
cnt = 0
for i in range(a, b + 1):
    result = solution(i)
    if len(result) == 1: continue
    if is_prime(len(result)) == True: cnt += 1
    else: continue

print(cnt)
        