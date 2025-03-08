import sys  
    
arr = []
for i in range(int(sys.stdin.readline())):
    arr.append(int(sys.stdin.readline()))

for i in sorted(arr):
    print(i)