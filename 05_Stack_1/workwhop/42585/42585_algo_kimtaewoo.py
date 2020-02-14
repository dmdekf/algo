# arrangement	            return
# ()(((()())(())()))(())	17

def solution(arrangement):
    answer = 0
    stack = 0
    for index, i in enumerate(arrangement):
        
        #레이저를 닫는 괄호일 경우 '('를 제거.
        if i == ')' :
            stack -= 1 
            #레이저가 아닌 경우 쇠막대기로 인식.
            if arrangement[index-1] == ')':
                answer += 1
            else:
                answer += stack
        else:
            stack += 1
    return answer