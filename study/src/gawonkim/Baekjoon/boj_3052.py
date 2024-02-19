# 파이썬 라이브러리 활용
# set이라는 집합 라이브러리를 이용해서 중복된 값들을 제거해줌
# 그리고 len 이라는 길이를 이용해서 중복된 값들이 제거된 집합의 길이를 구함

n_list = [0]*10

for i in range(10):
    num = int(input())
    n_list[i] = num % 42

counter = set(n_list)
print(len(counter))
