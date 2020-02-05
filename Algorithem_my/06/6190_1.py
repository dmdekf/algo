T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = list(map(int, input().split()))
    d= sorted(d, reverse=True)
    result = []
    for i in range(len(d)):
        diviede = d[i] % 10
        for j in range(2,len(i)+1):
            if d[i] % (10**j) >= diviede:
                d[i] = d[i]//10
        result
            else:
                break

        