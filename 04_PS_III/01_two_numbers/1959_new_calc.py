n = int(input())

for tc in range (1,n+1):
    ans = []
    len1,len2 = map(int,input().split())
    
    n1 = list(map(int,input().split()))
    n2 = list(map(int,input().split()))

    if len1 == len2:
        for i in range(0,len1):
            ans.append(n1[i] * n2[i])
    elif len1 > len2:
        for i in range(0,len1-len2+1):
            sum = 0
            for j in range(0,len2):
                sum += n2[j]*n1[j+i]
            ans.append(sum)
    else:
        for i in range(0,len2-len1+1):
            sum = 0
            for j in range(0,len1):
                sum += n1[j]*n2[j+i]
            ans.append(sum)
    print(f'#{tc} {max(ans)}')