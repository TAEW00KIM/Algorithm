import sys, heapq
input = sys.stdin.readline

arr = []

for i in range(int(input())):
    x = int(input())
    if x: 
        heapq.heappush(arr, x)
    else:
        if arr: print(heapq.heappop(arr))
        else: print(0)