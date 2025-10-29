import  math
from math import floor

n=int(input("nhap so nguyen duong n: "))
if n <= 2:
    print(0)
else:
    k= floor(math.sqrt(n))
print(k-1)

# hàm sẽ cho ra căn bậc 2 của số chính phương lớn nhất, ví dụ là 4 nếu có 4**2 thì sẽ tồn tại 1**2 2**2...,
# mà trường hợp 1**2 không là trường hợp đặc biệt không có ước chung là số lẻ nên khi in ra kết quả phải trừ 1