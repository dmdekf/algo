n =  1357

#단조증가 체크 함수 check()
def check(n):
    flag = True
    while n:
        n, r = n // 10, n % 10
        if n % 10 > r:
            return False
        
    return flag

  