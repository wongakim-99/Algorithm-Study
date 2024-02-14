num_list = list(map(int, input().split()))

if num_list[0]==num_list[1] and num_list[1]==num_list[2]:
    print(10000+1000*num_list[0])
elif num_list[0]==num_list[1]:
    print(1000+100*num_list[0])
elif num_list[1]==num_list[2]:
    print(1000+100*num_list[1])
elif num_list[0]==num_list[2]:
    print(1000+100*num_list[2])
else:
    max_val = max(num_list)
    print(100*max_val)