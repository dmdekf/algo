import sys
sys.stdin = open('input.txt')
from itertools import count

chk = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
T = int(input())
for tc in range(1, T+1):
    t, N = map(str,input().split())
    N = int(N)
    d = list(input().split())
    print('#{}'.format(tc))
    result = ''
    for i in chk.keys():
        result += (i+' ')*d.count(i)
    print(result[:-1])

