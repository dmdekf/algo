def sumnum(x, y):
    if len(x) > len(y):
        b = x
        s = y
    else:
        b = y
        s = x
    result = 0
    for i in range(len(b-s+1)):
        temp = 0
        for j in range(len(s)):
            temp += b[i+j]*s[j]
        if result < temp:
            result = temp
    return result


for tc in range(1, T+1):
    ans = []
    len1, len2 = map(int, input().split())

    d1 = list(map(int, input().split()))
    d2 = list(map(int, input().split()))
    result = sumnum(d1, d2)

    print(f'#{tc} {result}')
