num = int(input())
chr = "long"

for i in range(num//4):
    print(chr, end = " ")
print("int")

#print 내장 함수에서 end 파라미터의 기본값은 \n 이므로 문자열에 개행 문자를 덧붙인다
#end 파라미터의 값이 \n 이므로 문자열 끝에 개행문자가 추가된다

###줄바꿈 없이 출력하는 방법
###print함수의 end 파라미터의 값을 바꾸면, 기본적으로 줄 바꿈이 되어버리는 수행 결과를 변경가능
#end값을 " "로 설정하면 문자열 끝에 개행 문자\n대신에 공백이 추가됨,
##즉, 출력문 2개의 출력결과도 같은 줄에서 나타나게 됨