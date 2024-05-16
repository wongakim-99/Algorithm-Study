# import sys
# import math

# T = int(sys.stdin.readline())

# list = []
# for i in range(T):
#     N, M = map(int, sys.stdin.readline().split())
#     list.append(math.comb(M, N))

# for k in list:
#     print(k)




# 다른 방법 풀이
# 위에는 조합계산기인 math.comb 사용한 경우
# 조합 계산기 사용하지 않은 경우

'''
조합 공식 사용 -> nCr = n! / (n-r)! X r!
'''

import sys

def factorial(N):
    if N > 1:
        return (N * factorial(N - 1))
    else:
        return 1

list = []
T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    result = factorial(M) // (factorial(M - N) * factorial(N))
    list.append(result)

for k in list:
    print(k)