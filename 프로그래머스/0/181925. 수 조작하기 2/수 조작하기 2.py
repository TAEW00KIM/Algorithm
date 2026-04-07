def solution(numLog):
    ans = ''
    for i in range(len(numLog) - 1):
        if numLog[i + 1] == numLog[i] + 1:
            ans += 'w'
        elif numLog[i + 1] == numLog[i] - 1:
            ans += 's'
        elif numLog[i + 1] == numLog[i] + 10:
            ans += 'd'
        else:
            ans += 'a'
    return ans