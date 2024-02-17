#1 내 생각
n, x = map(int, input().split())
n_list = list(map(int,input().split()))
result_list = []

for i in range(n):
    if n_list[i] < x:
        result_list.append(n_list[i])
    else:
        continue

print(*result_list)


#2 join메서드 활용
n, x = map(int, input().split())
n_list = list(map(int,input().split()))
result_list = []
for i in range(n):
    if n_list[i] < x:
        result_list.append(str(n_list[i]))
    else:
        continue
result = ' '.join(result_list)
print(result)


#3 좀 더 단순코드
a,b = map(int,input().split())
n_list = list(map(int, input().split()))

for i in n_list:
    if i < b:
        print(i, end = " ")