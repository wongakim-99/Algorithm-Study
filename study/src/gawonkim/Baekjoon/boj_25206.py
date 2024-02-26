rating = ["A+","A0","B+","B0","C+","C0","D+","D0","F"]
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0
result = 0

for i in range(20):
    subject, stu_grade, stu_score = input().split() # 과목, 점수 , 등급 -> ex) 리눅스프로그래밍 3학점 A+
    stu_grade = float(stu_grade)
    if stu_score != 'P':
        total += stu_grade
        result += stu_grade * grade[rating.index(stu_score)]

print("%.6f" % (result/total))