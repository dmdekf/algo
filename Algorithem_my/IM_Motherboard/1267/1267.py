import sys
sys.stdin = open('input.txt')

T = 10
# 3 2
# 2 1 1 3
for tc in range(1, 11):
    N, M = map(int, input().split())
    d = list(map(int, input().split()))
    dd = []
    for j in range(0, len(d), 2):
        dd.append([d[j], d[j + 1]])
    # print(dd)
    result = dd.pop()
    while len(result) != N:
        for i in range(len(dd)):
            if result[-1] == dd[i][0]:
                result.append(dd[i][1])
                dd.pop(i)
                break
            elif result[0] == dd[i][1]:
                result.insert(0, dd[i][0])
                dd.pop(i)
                break
            elif dd[i][0] in result:
                result.append(dd[i][1])
                dd.pop(i)
                break
            elif dd[i][1] in result:
                result.insert(0, dd[i][0])
                dd.pop(i)
                break

    print('#{} '.format(tc), end='')
    print(*result)











