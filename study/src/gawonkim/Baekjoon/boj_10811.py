# 백준 바구니 뒤집기

N, M = map(int, input().split())
n_list = [i for i in range(1, N+1)]
temp = 0

for x in range(M):
    i, j = map(int, input().split())
    temp = n_list[i-1:j]
    temp.reverse()
    n_list[i-1:j] = temp

for x in range(N):
    print(n_list[x], end = ' ')