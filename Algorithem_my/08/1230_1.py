for tc in range(1, 11):
    N = int(input())
    origin = [i for i in input().split()]
    C = int(input())
    d = list(input().split())

    for i in range(len(d)):
        if d[i] == 'I':
            k = int(d[i+1])
            for j in range(i+3, i+3+int(d[i+2])):
                origin.insert(k, d[j])
                k += 1
        if d[i] == 'D':
            del origin[int(d[i+1]):int(d[i+1])+int(d[i+2])]

        if d[i] == 'A':
            origin.insert(len(origin), d[i+2:int(d[i+2])+int(d[i+1])])
    print('#{} {}'.format(tc, ' '.join(origin[0:10])))
