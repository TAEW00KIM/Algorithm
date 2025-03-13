from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
ans = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = ''.join(list(map(str, reversed(list(j)))))
        ans.append(int(num))

ans.sort()
try: print(ans[n - 1])
except: print(-1)