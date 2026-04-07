def solution(myString):
    sp = myString.split('x')
    print(sp)
    ans = []
    for i in sp:
        ans.append(len(i))
    return ans