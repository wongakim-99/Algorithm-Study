time, min = input().split()
cooking_time = input()

time = int(time)
min = int(min)
cooking_time = int(cooking_time)

'''cooking_time(요리시간)은 분으로만 표시됨
   이걸 분+요리시간 더한 값에 60을 나눈 몫과 나머지를 더하기만 하면됨
   시간이23넘어가는지 안넘어가는지에따라 0시가 될지는 조건문 걸고 판단'''
time += (min+cooking_time)//60
if time > 23:
    time -= 24
    print(str(time)+" "+str((min+cooking_time)%60))
else:
    print(str(time)+" "+str((min+cooking_time)%60))
