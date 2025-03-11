num = int(input())
numbers = list(map(int, input().split()))
numbers = set(numbers)
numbers = list(numbers)
numbers.sort()
for i in numbers:
    print(i, end = ' ')