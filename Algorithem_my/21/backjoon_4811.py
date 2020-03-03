import sys
sys.stdin = open('4811_input.txt')

def f(w, h):
    if w < 0:
        return 0
    if w == 0 and h == 0:
        return 1
    if D[w][h] > 0:
        return D[w][h]
    if w > 0:
        D[w][h] +=f(w-1,h+1)
    if h > 0:
        D[w][h] +=f(w,h-1)

    return D[w][h]


n = int(sys.stdin.readline().strip())
while n:
    D = list([0]*(2*n) for _ in range(2*n))

    print(f(n,0))
    n = int(sys.stdin.readline().strip())