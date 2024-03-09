# 직사각형은 경계선까지의 거리 고려에서 대각선이 최소인 경우가 없으므로 
# 대각선은 고려하지 않아야 한다

x, y, w, h = list(map(int, input().split()))
print(min([x, y, w - x, h - y]))