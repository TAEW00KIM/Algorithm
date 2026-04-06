def solution(rny_string):
    if 'm' not in rny_string: return rny_string
    for i in rny_string:
        if i == 'm':
            rny_string = rny_string.replace('m', 'rn')
    return rny_string