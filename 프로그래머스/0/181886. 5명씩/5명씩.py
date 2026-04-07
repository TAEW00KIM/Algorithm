def solution(names):
    ans = []
    for i in range(len(names)):
        if i % 5 == 0 or i == 0:
            ans.append(names[i])
    return ans