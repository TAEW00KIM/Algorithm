def solution(strArr):
    ans = []
    for i in strArr:
        if 'ad' not in i:
            ans.append(i)
    return ans