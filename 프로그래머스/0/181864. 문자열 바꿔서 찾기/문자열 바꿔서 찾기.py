def solution(myString, pat):
    flipped = ''.join('B' if c == 'A' else 'A' for c in myString)
    return int(pat in flipped)