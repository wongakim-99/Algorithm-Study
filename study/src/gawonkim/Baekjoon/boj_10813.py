#백준 공 바꾸기

N, M = map(int, input().split())
bucket = [i for i  in range(1, N+1)]
temp = 0

# 10~12 ***swap생각***
for i in range(M):
    i,j = map(int, input().split())
    temp = bucket[i-1]
    bucket[i-1] = bucket[j-1]
    bucket[j-1] = temp

for i in range(N):
    print(bucket[i], end = ' ')


'''
****참고****
두 변수에 저장된 자리를 체인지 할때 
10~12와 같이 많이 저런식으로 자리를 바꿈
정렬 알고리즘인 삽입정렬, 버블정렬 기타등등...에서 많이 나옴!
그리고 다른 정렬 알고리즘에서도 종종 많이 봤음!
잘 참고해서 알아두면 나쁘지 않다!
'''