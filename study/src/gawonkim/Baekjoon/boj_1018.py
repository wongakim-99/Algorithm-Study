n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(input())

# 문제 규칙상 칠할 체스는 8x8 크기로 정해져 있으므로 n-7과 m-7 범위의 중첩 for문을 작성한다.
for i in range(n-7):    # i, j는 체스판의 칠할 부분을 찾는 시작점
    for j in range(m-7):
        draw1 = 0
        draw2 = 0

        # 이후 시작점부터 8x8크기의 체스판을 탐색하여 칠할 개수를 찾아주기 위해 시작점인 i, j지점부터
        # i+8, j+8 범위의 중첨 for문을 작성함    
        for a in range(i, i+8):
            for b in range(j, j+8):
                if(a+b) % 2 == 0:   # 만약 a+b를 2로 나눈 나머지가 0이라면, draw1은 검은색이 아닐 때 1을 더하여 색칠
                    # draw2는 흰색이 아닐 때 1을 더하여 칠함
                    if board[a][b] != "B":
                        draw1 += 1
                    if board[a][b] != "W":
                        draw2 += 1
                else:
                    if board[a][b] != "W":
                        draw1 += 1
                    if board[a][b] != "B":
                        draw2 += 1
        
        result.append(draw1)
        result.append(draw2)

print(min(result))