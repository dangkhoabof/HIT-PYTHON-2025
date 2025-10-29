import re
chon="C"
Email_array=[]
while chon.upper() == "C":
    email=input("enter your email: ")
    Email_array.append(email)
    chon=input("có muốn tiếp tục nhập không(C/K): ")


print("email có hợp lệ hay không")

pattern = r'^\w+@\w+\.\w+$'
for i in Email_array:
    if re.match(pattern, email):
        print(f"\"{i}\" hợp lệ")
    else:
        print(f"\"{i}\" không hợp lệ")
