receipt_total_price = int(input())  #영수증에 적힌 전체 가격
product_type = int(input())   #물건종류

temp_sum = 0    #내가 계산해본 전체 가격
for i in range(product_type):
    product_price, product_count = map(int,input().split()) #각 물건가격, 각 물건개수
    temp_price = product_price*product_count    #내가 계산한 각 물건가격x각 물건개수
    temp_sum += temp_price  #내가 계산한 물건전체 가격

if temp_sum == receipt_total_price:
    print("Yes")
else:
    print("No")