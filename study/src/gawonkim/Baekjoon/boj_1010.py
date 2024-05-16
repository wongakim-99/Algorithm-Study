import sys
import math

T = int(sys.stdin.readline())

list = []
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    list.append(math.comb(M, N))

for k in list:
    print(k)