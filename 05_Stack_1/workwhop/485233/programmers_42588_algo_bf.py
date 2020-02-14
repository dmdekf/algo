# 완전 탐색 
# 송신 탑(높이)	수신 탑(높이)
# 5(4)	4(7)
# 4(7)	2(9)
# 3(5)	2(9)
# 2(9)	-
# 1(6)	-
def solution(heights):
    answer = []
    for i in range(len(heights)):
        for j in range(i,-1,-1):
            if heights[i] < heights[j]:
                answer.append(j+1)
                break
            else:
                answer.append(0)
                
    return answer

def solution(h):
    ans = [0] * len(h)
    for i in range(len(h)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if h[i] < h[j]:
                ans[i] = j+1
                break
    return ans
