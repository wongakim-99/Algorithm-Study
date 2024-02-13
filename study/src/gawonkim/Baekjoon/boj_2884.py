'''case1 : 만약 분이 45분 이상이면 시간은 그대로 분에서 45만 빼면 끝
   case2 : 만약 분이 45분 미만이면 시간에서 1빼고 60 - (45-분)
   case3 : 만약 시간이 0시 이다 그러면 시간을 0 -> 23으로 변경'''

clock, min = input().split()
clock = int(clock)
min = int(min)

if min >= 45:
    new_min = min-45
    print(str(clock)+" "+str(new_min))
else:
    if clock == 0:
        new_min = 60 - (45 - min)
        print(str(23)+" "+str(new_min))
    else:
        new_clock = clock - 1
        new_min = 60 - (45 - min)
        print(str(new_clock)+" "+str(new_min))
