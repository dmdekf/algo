def f(n, k, s, M):
    global M
    if s == M:
        cnt += 1
        return
    elif n == k:
        return
    else:
        f(n+1, k, s+A[n], M)
        f(n+1, k, s, M)
