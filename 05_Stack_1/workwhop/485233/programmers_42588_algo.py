# 송신 탑(높이)	수신 탑(높이)
# 5(4)	4(7)
# 4(7)	2(9)
# 3(5)	2(9)
# 2(9)	-
# 1(6)	-
def solution(heights):
    stack = []
    answer = []
    for i in range(len(heights)):
        stack = []
        for j in range(i):
            if heights[i] < heights[j]:
                stack.append(j+1)
        if stack:
            answer.append(stack.pop())
        else:
            answer.append(0)

    return answer