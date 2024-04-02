# 백준은 아니고... 본인 2학년 2학기 알고리즘 실습 시간에 배웠던 하노이 타워 문제
# 문제 : 하노이 타워를 순환호출 형식으로 작성하시오
# 출력예시 : 원판을 ~ 에서 ~ 으로 옮긴다.

def hanoiTower(n, A, B, C): 
    if n == 1:
        print(1, "원판을", A, "에서", C," 로 옮긴다.")
    else:
        hanoiTower(n - 1, A, C, B)
        print(n, "원판을", A, "에서", C," 로 옮긴다.")
        hanoiTower(n - 1, B, A, C)

def __main__():
    hanoiPlate = int(input("원판의 개수 입력 : "))
    hanoiTower(hanoiPlate, 'A', 'B', 'C')

__main__()