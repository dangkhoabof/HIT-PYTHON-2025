n=int(input("Nhap so lượng học sinh: "))
hocvien=[]
for  i in range(n):
    print(f"nhap thông tin học sinh thứ {i+1}: ")
    ten=input("nhập tên học sinh: ")
    kt1= int(input("nhap diem kiem tra tx1: "))
    kt2= int(input("nhap diem kiem tra tx2: "))
    tong=kt1+kt2
    if tong>200:
        hocluc="Xuất xắc"
    elif tong>150:
        hocluc="giỏi"
    elif tong>100:
        hocluc="khá"
    else:
        hocluc="yếu"

    hocvien.append({
        'stt': i+1,
        'ten': ten,
        'tong': tong,
        'hocluc': hocluc,
    })
print("danh sách sinh viên:")
print("="*50)
print(f"{'STT':<4} {'Tên':<20} {'Tổng':<10} {'Học lực':<10}")
for hs in hocvien:
    print(f"{hs['stt']:<4} {hs['ten']:<20} {hs['tong']:<10} {hs['hocluc']:<10}")
