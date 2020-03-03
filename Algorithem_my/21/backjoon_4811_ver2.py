import sys
sys.stdin = open('4811_input.txt')

n = int(sys.stdin.readline().strip())
while n:
    r = 1
    for i in range(2 * n, n, -1):
        print(i)
        r *= i
    for i in range(1, n + 2):
        print(i)
        r //= i
    print(r)
    n = int(sys.stdin.readline().strip())

# n = int(sys.stdin.readline().strip())
# while n:
#     r = 1
#     for n in range(2 * n, n, -1):
#         print(n)
#         r *= n
#     for n in range(1, n + 1):
#         print(n)
#         r //= n
#     print(r)
#     n = int(sys.stdin.readline().strip())
