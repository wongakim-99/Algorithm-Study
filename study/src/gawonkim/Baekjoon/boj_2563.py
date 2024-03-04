N = int(input())
arr = [[0]*100 for i in range(100)]
for _ in range(N):
    y1, x1 = map(int, input().split())

    for z in range(x1, x1 + 10):    #세로돌기
        for j in range(y1, y1 + 10):    # 가로돌기
            arr[z][j] = 1   # 해당 범위 값을 0에서 1로 바꿔줌

result = 0  # 넓이를 출력할 변수
for k in range(100):
    result += arr[k].count(1)   # 1 개수만 세어줌

print(result)