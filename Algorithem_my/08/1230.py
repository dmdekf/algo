import sys

sys.stdin = open('input1230.txt')


for tc in range(1, 11):
    N = int(input())
    origin = list(input().split())
    C = int(input())
    d = list(input().split())

    for i in range(len(d)):
        temp = ''
        if d[i] == 'I':
            d.pop(i)
            locanum = int(d.pop(i))
            numnum = int(d.pop(i))
            for _ in range(numnum):
                origin.insert(locanum+1, d.pop(i))

        if d[i] == 'D':
            print(d.pop(i))
            print(d.pop(i))
            print(d.pop(i))
            print(d.pop(i))
            print(d.pop(i))
            print(d.pop(i))
            # lonum = int(d.pop(i))
            # numd = int(d.pop(i))
            for _ in range(numd):
                origin.pop(lonum+1)

        if d[i] == 'A':
            d.pop(i)
            numa = int(d.pop(i))
            for k in range(numa):
                temp += d.pop(k)
            origin.append(temp)

    print(origin[0:11])
