#파이썬 라이브러리 활용

num_list = []
for i in range(9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list))+1)
