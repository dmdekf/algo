import sys
sys.stdin = open('input.txt')

n = int(input())
length = 0
for i in range(n//2+1,n+1):
    num = [n, i]
    while num[-2] - num[-1] >= 0:
        num += [num[-2] - num[-1]]
        if num[-2] - num[-1]<0:
            break
    if length < len(num):
        length = len(num)
        result = num
print(length)
print(*result)







