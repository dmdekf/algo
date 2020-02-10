import sys
sys.stdin = open('input.txt')
def checkd(word):
    if word == word[::-1]:
        return True
    return False
T = 10
for _ in range(T):
    n = int(input())
    d = [list(input()) for _ in range(100)]
    cold = []
    for i in range(100):
        temp = ''
        for j in range(100):
            temp += d[j][i]
        cold.append(temp)
    num = 101
    chk = 1
    while num >=1 and chk ==1:
        num -=1
        for k in range(100):
            for j in range(0,100-i+1):
                if checkd(d[k][j:j+num]) or checkd(cold[k][j:j+num]):
                    chk = 0

    print('#{} {}'.format(n,num))




