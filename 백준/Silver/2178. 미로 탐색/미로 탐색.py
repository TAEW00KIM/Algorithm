import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input().rstrip())))
    
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] == 1:
                q.append((nx, ny))
                miro[nx][ny] = miro[x][y] + 1
                
    return miro[n-1][m-1]


print(bfs(0, 0))