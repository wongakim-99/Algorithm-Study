# A = 올라갈 수 있는 거리, B = 미끄러지는 거리, C = 나무막대 높이
# 올라가야할 거리 = C - B
# 하루에 올라갈 수 있는 거리 = A - B

A, B, C = map(int, input().split())

if (C - B) % (A - B) == 0:
    print((C - B) // (A - B))   # 하루
else:
    print((C - B) // (A - B) + 1)   # 하루 + 1