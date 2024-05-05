import sys

N, K = map(int, sys.stdin.readline().split())
queue = []
arr = [i for i in range(1, N + 1)]
idx = 0

for i in range(N):
    idx += K - 1
    if idx >= len(arr):
        idx %= len(arr)
    queue.append(str(arr[idx]))
    arr.pop(idx)

print("<",", ".join(queue),">",sep="")