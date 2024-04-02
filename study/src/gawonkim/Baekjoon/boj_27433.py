# 팩토리얼 -- 재귀로 구현

def factorial(n):
    if n <= 1:
        ans = 1
    else:
        ans = factorial(n-1) * n
    return ans

def main():
    print(factorial(int(input())))

main()