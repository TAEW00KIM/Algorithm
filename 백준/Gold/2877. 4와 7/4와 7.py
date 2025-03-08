import sys
num = int(sys.stdin.readline())
result = ''
while num > 0:
    odd = num % 2
    num //= 2
    if odd == 0:
        num -= 1
        result = '7' + result
    else:
        result = '4' + result

print(result)
    