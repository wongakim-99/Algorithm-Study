#1 최대, 최소 라이브러리 활용
n = int(input())
n_list = list(map(int, input().split()))

max_value = max(n_list)
min_value = min(n_list)

print(min_value, max_value)


#2 최대, 최소 라이브러리 활용x
n = int(input())
n_list = list(map(int,input().split()))

min = n_list[0]
max = n_list[0]

for i in n_list[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min,max)
