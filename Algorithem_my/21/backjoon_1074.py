import sys
sys.stdin = open('1074_input.txt')


def f(x, y, l):
    global result
    if x == r and y == c:
        return print(int(result))
    # if l == 1:
    #     result += 1
    #     return
    if not(x <= r and r < x+l and y <= c and c < y+l):
        result += l*l
        return
    f(x, y, l/2)
    f(x, y+l/2, l/2)
    f(x+l/2, y, l/2)
    f(x+l/2, y+l/2, l/2)


n, r, c = map(int,sys.stdin.readline().strip().split())
print(n,r,c)
result = 0
f(0, 0,pow(2,n))
