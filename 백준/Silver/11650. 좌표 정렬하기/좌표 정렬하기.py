import sys
input = sys.stdin.readline

xy = []
for i in range(int(input())):
    x, y = input().split()
    xy.append([int(x), int(y)])

for i in sorted(xy):
    print(i[0], i[1])