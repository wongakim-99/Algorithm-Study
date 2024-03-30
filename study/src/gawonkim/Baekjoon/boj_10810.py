#백준 10810 공 넣기

# N, M = map(int, input().split())    #N = 바구니 개수, M = 공을 넣을 횟수
# bucket = [0]*(N+1)

# for a in range(M):
#     i,j,k = map(int,input().split())
#     for n in range(i, j+1):
#         bucket[n] = k

# for i in range(1, N+1):
#     print(bucket[i], end = ' ')


N, M = map(int, input().split())
bucket = [0]*(N+1)

for a in range(M):
    i,j,k = map(int, input().split())
    for q in range(i, j+1):
        bucket[q] = k

for z in range(1,N+1):
    print(bucket[z], end = ' ')