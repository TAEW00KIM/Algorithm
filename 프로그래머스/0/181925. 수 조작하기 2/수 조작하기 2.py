def solution(numLog):
    return ''.join({
        1: 'w', -1: 's', 10: 'd', -10: 'a'
    }[b - a] for a, b in zip(numLog, numLog[1:]))