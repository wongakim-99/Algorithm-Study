# 백준 2839 설탕배달

sugar = int(input())

bag = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bag += (sugar // 5) # 5의 배수이면
        print(bag)  # 5로 나눈 몫을 구해야 정수가 됨
        break
    sugar -= 3
    bag += 1    # 5의 배수가 될 때까지 설탕 -3, 봉지 +1

else:
    print(-1)
