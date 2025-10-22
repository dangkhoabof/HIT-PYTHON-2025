print("chao mung de CLB Tin Hoc HIT")
print('CLB Tin Hoc HIT truc thuoc Truong CNTT - "10 diem"')
chuoi="CLB Tin Hoc HIT truc thuoc Truong CNTT"
for s in chuoi:
    if s.isupper():
        print(s, end=" ")
print()
for s in chuoi:
    if s.islower():
        print(s, end=" ")
print()
print("chuoi co tu CNTT khong:",end=" ")
if "CNTT" in chuoi:
    print("yes")
else:
    print("no")
print("doi chu hoa voi chu thuong: ",chuoi.swapcase())
iouhc=""
for s in chuoi:
    if s.isupper():
        iouhc+=s.lower()
    elif s.islower():
        iouhc+=s.upper()
    else:
        iouhc+=s
print(iouhc)

