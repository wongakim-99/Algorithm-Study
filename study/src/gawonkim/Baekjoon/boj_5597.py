# 교실에 학생들 30명 저장

class_student = [i for i in range(1, 31)]

for i in range(28):
    student_number = int(input())
    class_student[student_number-1] = 0

for _ in range(30):
    if class_student[_] != 0:
        print(_+1)

'''
내 생각

1. class_student 라는 배열을 선언하고 1부터 30까지 저장
2. (5~7) 입력받은 수가 만약에 1~30사이에 존재하는 수라면 해당 인덱스를 0으로 초기화
3. (9~11) class_student라는 배열을 돌면서 만약에 0이 아닌 친구가 있다면 그놈이 과제 안낸 범인
'''

