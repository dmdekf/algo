
# 1
# 4
# 2 4 7 10	// 테스트케이스 개수, T=1
# // N=4
# // A1=2, A2=4, A3=7, A4=10

# #1 28

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = list(map(str, input().split()))
    temp = []
    check = False
    for i in d:
        if len(i) > 1 :
            for j in range(len(i)-1):
                if i[j] <= i[j+1]:
                    check = True
                else:
                    check = False
                    break
            if check:
                temp.append(i)
        else:
            temp.append(i)
    result = []
    for k in temp:
        result.append(int(k))
    
    if temp == []:
        big = -1
    else:
        big=sorted(result)[-1] * sorted(result)[-2]
    
    print('#{} {}'.format(tc, big))