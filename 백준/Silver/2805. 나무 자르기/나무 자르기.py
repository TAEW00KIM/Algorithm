import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
trees = Counter(map(int, input().split()))

s, e = 1, 1000000000

while s <= e:
    mid = (s + e) // 2
    tot = sum((h - mid) * i for h, i in trees.items() if h > mid)
    
    if tot >= m: s = mid + 1
    elif tot < m: e = mid - 1
    
print(e)