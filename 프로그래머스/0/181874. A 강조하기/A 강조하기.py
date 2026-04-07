def solution(myString):
    for i in myString:
        if i == 'a':
            myString = myString.replace(i, 'A')
        elif i.isupper() and i != 'A':
            myString = myString.replace(i, i.lower())
    return myString