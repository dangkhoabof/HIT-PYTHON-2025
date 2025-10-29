print("Hướng dẫn: Nhập 'pass' để giữ chỗ, 'skip' để bỏ qua, 'x' hoặc 'X' để kết thúc.")
don_hang=[]
tongTien=0
soMon=0
while True:
    tenMon=input("nhập tên món: ")
    if tenMon.lower()=="x":
        break
    if tenMon.lower()=="skip":
        continue
    if tenMon.lower()=="pass":
        pass
        don_hang.append({'ten':"giu cho",'gia':"giu cho"})
        soMon=soMon+1
    else:
        giaMon = float(input("nhập giá cho món ăn: "))
        don_hang.append({'ten': tenMon, 'gia': giaMon})
        tongTien = tongTien + giaMon
        soMon = soMon + 1
print("món ăn đã gọi")
print("="*50)
print(f"'{'tên':<20} giá")
for i in don_hang:
    print(f"{i['ten']:<20} {i['gia']}")
print("="*50)
print("số món đã gọi: ",soMon)
if tongTien>200000:
    print("do hóa đơn lớn hơn 200000 nên đụược giảm giá 10%: ",tongTien*0.1)
    print("số tiền phải trả là: ",tongTien*0.9)
else:
    print("số tiền phải trả là:  ", tongTien)