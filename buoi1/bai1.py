a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

print("a+b =",a+b)
print("a-b =",a-b)
print("a*b =",a*b)
print("a//b =",a//b)
print("a ** b =",a**b)
print("a%b=" ,a%b)

if a > b:
    print("a lớn hơn b")
elif a < b:
    print("a nhỏ hơn b")
else:
    print("a bằng b")

print("a AND b =", a & b)
print("a OR b =", a | b)
print("a XOR b =", a ^ b)
print("NOT (a == b) =", not (a == b))
print("a >> 5 =", a >> 5)
print("a << 6 =", a << 6)

bin_a = bin(a)[2:]
reversed_bin_a = bin_a[::-1]
print("Hệ nhị phân đảo ngược của a là:", reversed_bin_a)