# import sys

# sys.stdin = open('input.txt')


def calcx(num):
    return num + calcx(num-1) if num != 1 else 1
def sumy(num,y):
    return sumy(num,y-1)+1 if y > 2  else num if y == 2 else 0
def calcy(num, y):
    return calcy(num, y-1)+sumy(num,y) if y > 1 else calcx(num)
print(calcy(5,5))
# T = int(input())
# for tc in range(1,T+1):
#     p, q = map(int,input().split())
#     result = []
#     for i in range(1,10000):
#         for j in range(1,10000):
#             if calcy(i,j)==p:
#                 result.append((i,j))
#                 print(result)
#                 break
# #                 p1=i
# #                 p2=j
# #                 print(p1,p2)
            
# #     for i in range(1,10000):
# #         for j in range(1,10000):
# #             if calcy(i,j)==q:
# #                 q1=i
# #                 q2=j
#     # print(p1,p2, q1,q2)