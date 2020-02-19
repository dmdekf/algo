def f(n, k, s):
    if n == k:
        if s == 10:
    elif s > 10:
        return

    else:
        L[n] =1
        f(n+1, k, s+A[n])
        L[n] = 0
        f(n+1, k, s)


A = [1,2,3,4,5,6,7,8,9,10]
L = [0]*len(A)
f(0,len(A),0)


