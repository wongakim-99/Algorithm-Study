import sys

num = int(sys.stdin.readline())

for i in range(num):
    a,b = map(int, sys.stdin.readline().split())    #한 줄에 두 개 이상의 값을 입력받는 방법
    print(a+b)

'''
input()을 사용하면 종종 시간초과 에러가 뜰 때가 있다.
이를 방지하기 위해서 sys.stdin.input()을 사용했다.

input()이 sys.stdin.readline() 보다 느린이유

1. input()은 매개변수로 prompt message를 받는다. (따라서 입력을 받기 전에 prompt message를
출력해야 한다.)
2. 입력받은 값의 개행 문자를 삭제시키고 반환한다.

이러한 단계를 거치기 때문에 input()은 비교적 속도가 느리다.

sys.stdin.readline()의 특징
문자열로 입력을 받는다.

sys.stdin.readline()은 문자열로 입력을 받는다.
따라서 만약 입력받은 문자열을 정수 혹은 실수, 리스트로 사용할 때는 적절히 함수를 사용하여
처리를 해줘야 한다.

개행문자 \n 을 같이 입력받는다. 
ex) 만약 "Hello, World!"라는 문자열을 입력받았다고 가정하면
sys.stdin.readline() 의 입력으로는 "Hello, World!\n"가 들어온다.
'''