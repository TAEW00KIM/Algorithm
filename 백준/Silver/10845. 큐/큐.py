import sys

q = []
for i in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()
    if 'push' in cmd: q.append(int(cmd[-1]))
    elif 'pop' in cmd:
        if len(q) == 0: print(-1)
        else: print(q.pop(0))
    elif 'size' in cmd:
        print(len(q))
    elif 'empty' in cmd:
        if len(q) == 0: print(1)
        else: print(0)
    elif 'front' in cmd:
        if len(q) == 0: print(-1)
        else: print(q[0])
    elif 'back' in cmd:
        if len(q) == 0: print(-1)
        else: print(q[-1])