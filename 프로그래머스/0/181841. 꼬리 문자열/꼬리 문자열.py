def solution(str_list, ex):
    ans = ''
    for i in range(len(str_list)):
        if ex in str_list[i]: continue
        ans += str_list[i]
    return ans