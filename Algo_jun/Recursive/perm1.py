def f(n, k, m):
    if n == k: #순열 1개 완성
        print(*p[:-2],sep=' ')
    else:
        for i in range(m): #used 를 왼쪽부터 탐색
            if u[i] == 0: #사용한 숫자가 아니면
                u[i] = 1
                p[n] = A[i]
                f(n+1,k,m)
                u[i] = 0

A = [1, 2, 3, 4, 5]
p = [0]*len(A)
u = [0]*len(A)

f(0,3, len(A))