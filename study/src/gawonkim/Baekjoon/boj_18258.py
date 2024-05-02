def hanoiTower(n, start, end):
    if n == 1:
        print(start, end)
    else:
        hanoiTower(n - 1, start, 6 - start - end)
        print(start, end)
        hanoiTower(n - 1, 6 - start - end, end)

def __main__():
    plate = int(input())
    print(2**plate - 1)
    hanoiTower(plate, 1, 3)

if __name__ == "__main__":
    __main__()
