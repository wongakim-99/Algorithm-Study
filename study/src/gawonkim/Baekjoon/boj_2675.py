# Case = int(input())

# for i in range(Case):
#     N, S = map(str, input().split())
#     N = int(N)
#     S = list(S)
#     for j in range(len(S)):
#         print(S[j] * N, end = '')
#     print('')

case = int(input())

for i in range(case):
    n, s = map(str, input().split())
    n = int(n)
    s = list(s)
    for j in range(len(s)):
        print(s[j] * n, end = '')
    print('')


