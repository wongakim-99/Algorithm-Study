# 영문자 아스키코드값과 입력받은 문자의 아스키코드 값을 비교해서 푼 문제

alphabet = [-1] * 26    # 알파벳 26자 담을 배열 선언
fir_alpha = 97  # 영어 소문자 첫번째 a의 아스키 코드값이 97
new_arr = [] * 26   # 나중에 초기화 시키고 새로 담을 배열

string = input()
length = len(string)

for i in range(26): # 알파벳 배열에 아스키코드값 넣음
    alphabet[i] = fir_alpha
    fir_alpha += 1

for i in range(26):
    count = 0
    for j in range(length):
        if alphabet[i] == ord(string[j]):
            count = 1
            new_arr.append(j)
            break
    if not count:
        new_arr.append(-1)

for element in new_arr:
    print(element, end = ' ')



# 풀고 보니 코드가 너무 C언어스러워서...파이썬 라이브러리를 활용한 버전
string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
# 반복문으로 알파벳의 존재 유무를 확인하기 위해 사용할 알파벳들이 존재하는 alphabet 선언

for i in alphabet:
    if i in string:
        print(string.index(i), end = ' ')
    else:
        print( -1, end = ' ')