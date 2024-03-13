# 수 정렬하기2
# 병합정렬 알고리즘 사용(merge sort)

# 배열을 절반으로 자르는 과정(Devide)
def merge_sort(arr):
    if len(arr) <= 1:   # 만약 리스트가 0또는 1인 경우 정렬된 경우임
        return arr  # 그래서 리턴값을 배열로 반환
    
    mid = len(arr) // 2
    left = arr[:mid]    # 왼쪽 리스트를 인덱스 0부터 배열의 중간까지 자름
    right = arr[mid:]   # 오른쪽 리스트를 인덱스 중간부터 배열의 끝까지 자름

    left = merge_sort(left) # 재귀호출을 통해 왼쪽 부분분할
    right = merge_sort(right)   # 재귀호출을 통해 오른쪽 부분분할

    return merge(left, right)   

# 분할된 배열을 다시 합치는 과정
def merge(left, right):
    result_arr = []
    left_idx, right_idx = 0, 0

    # 두 개의 배열 left 와 right을 병합하는 과정에서 
    #현재 인덱스를 가리키는 포인터(left_idx와 right_idx)를 사용하여 
    #두 배열의 값을 비교하고 작은 값을 result_arr에 추가하는 부분(26~32)
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:   
            result_arr.append(left[left_idx])
            left_idx += 1
        else:
            result_arr.append(right[right_idx])
            right_idx += 1
    
    #while 루프는 왼쪽 배열(left)의 모든 요소를 이미 비교하여 추가했으나, 
    #오른쪽 배열(right)에 남은 요소가 있는 경우(35~37)
    while left_idx < len(left):
        result_arr.append(left[left_idx])
        left_idx += 1
    
    # 마찬가지
    while right_idx < len(right):
        result_arr.append(right[right_idx])
        right_idx += 1
    
    return result_arr

if __name__ == "__main__":
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(int(input()))
    
    sorted_numbers = merge_sort(numbers)
    for num in sorted_numbers:
        print(num)

'''
병합정렬 알고리즘 사용

병합정렬이란? 

병합정렬(merge sort)
-> 안정 정렬에 속하며, 분할 정복 알고리즘의 하나
   문제를 작은 2개의 문제로 분리한 다음 각각을 해결하고 결과를 모아서 원래의 문제를 해결하는 전략
   (**분할 정복 방법은 대개 순환 호출을 이용하여 구현)

   
1. 리스트의 길이가 0또는 1이면 정렬된 것으로 본다
2. 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다
3. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬
4. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병


● 병합 정렬은 다음의 단계들로 이루어짐
    1. 분할(Divide) : 입력된 배열을 같은 크기의 2개의 부분 배열로 분할.
    2. 정복(Conquer) : 부분 배열을 정렬. 부분 배열의 크기가 충분히 작지않은경우 
    순환호출을 이용하여 다시 분할 정복 방법 적용
    3. 결합(Combine) : 정렬된 부분 배열들을 하나의 배열에 합병

예시ex)

                        21  10  12  20  25  13  15  22
                             /                  \ 
       Devide               /                    \ 
                    (21  10  12  20)       (25  13  15  22)
                      /      \                 /     \ 
       Devide        /        \               /       \ 
                 (21 10)      (12  20)    (25   13)  (15  22)
       Devide     /   \         /   \        /  \       /   \ 
                21     10     12    20      25   13    15   22

                  이제 여기서 더 이상 쪼갤수가 없으니 합치기 시작
***************************************************************************
                   \    /      \    /      \   /       \    /       
       Combine    (10  21)    (12  20)    (13  25)    (15  22)
                       \        /              \         /
       Combine       (10  12  20  21)         (13  15  22  25)
                            \                     /
       Combin                \                   /
                        (10  12  13  15  20  21  22  25)
                    
                    이 정렬된 리스트를 또 다른 리스트에 복사

합칠때(Combine) 할 때는 작은 숫자가 앞에 큰 숫자를 뒤에 위치시킨다

**배열에 27, 10, 12, 20, 25, 13, 15, 22 가 저장되어 있다고 가정하고 자료를 오름차순으로 정렬해보자**
->2개의 정렬된 리스트를 합병(merge)하는 과정

1. 2개의 리스트의 값들을 처음부터 하나씩 비교하여 두 개의 리스트의 값 중에서 
더 작은 값을 새로운 리스트로 옮긴다.

2. 둘 중에서 하나가 끝날 때까지 이 과정을 되풀이한다.

3. 만약 둘 중에서 하나의 리스트가 먼저 끝나게 되면 나머지 리스트의 값들을 전부 새로운 리스트
(sorted)로 복사한다.

4. 새로운 리스트(Sorted)를 원래의 리스트(list)로 옮긴다.

'''