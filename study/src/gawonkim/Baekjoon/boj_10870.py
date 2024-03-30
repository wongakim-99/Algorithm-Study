# 피보나치 수열
# 재귀로 풀이

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

def main():
    n = int(input())
    print(fibo(n))

main()
