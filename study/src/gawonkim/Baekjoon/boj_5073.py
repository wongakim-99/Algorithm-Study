while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0 :
        break
    if sum((a, b, c)) - max((a, b, c)) <= max((a, b, c)):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")

'''
"sum((a, b, c)) - max((a, b, c))" <- 이게 포인트
" 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다."(문제내용 참고)

일단 5번째 라인에 삼각형 조건에 만족하지 못하는걸 먼저 거르고 시작하면
    
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")

이 부분에서 이등변 삼각형인지 아니면 그냥 삼각형인지 알아서 판단됨.
만약 세 변의 길이가 다 같은 정삼각형이면 첫번째 조건 "if sum((a, b, c)) - max((a, b, c)) <= max((a, b, c))" 에서 알아서 걸러질테고
그러면 두 변의 길이가 같은 이등변 삼각형 혹은 세 변의 길이가 다 다른 그냥 삼각형인데
"elif a == b or b == c or a == c:" 이 조건으로 해결
▲여기서 하나라도 같으면 이등변 삼각형이므로 빠져나갈거고, 아니면은 그 밑에 다 다른 길이의 변인 그냥 삼각형인 다음 조건으로 넘어갈거임
'''