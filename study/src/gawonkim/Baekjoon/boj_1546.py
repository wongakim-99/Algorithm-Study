subject = int(input())
grade = list(map(int, input().split()))
max_grade = max(grade)

for i in range(subject):
    grade[i] = (grade[i]/max_grade)*100

print(sum(grade)/subject)