num = int(input())
numbers = set(map(int, input().split()))
numbers = list(numbers)
numbers.sort()
for i in numbers:
    print(i, end = ' ')