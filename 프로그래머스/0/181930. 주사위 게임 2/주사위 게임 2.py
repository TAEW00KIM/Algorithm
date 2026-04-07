def solution(a, b, c):
    s1 = a + b + c
    s2 = a*a + b*b + c*c
    s3 = a*a*a + b*b*b + c*c*c
    
    count = len({a, b, c})
    
    if count == 3:
        return s1
    elif count == 2:
        return s1 * s2
    else:
        return s1 * s2 * s3