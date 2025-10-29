n=int(input("nhap n: "))
x=int(input("nhap x: "))
tong = 0
giaithua =1
s=0
luythua=1
for i in range(n+1):
    tong=tong+luythua/giaithua
    s= s + 1/giaithua
    luythua=luythua*x
    giaithua=giaithua*(i+1 if i+1>0 else 1)
print("tong cua bieu thuc 1 la: ",tong)
print("tong cua bieu thuc 2 la:  ",s)