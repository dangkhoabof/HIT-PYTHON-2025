chuoi=input("nhap 1 chuoi: ").lower()
dem={}
for i in chuoi:
    if i.isalpha():
        dem[i]=chuoi.count(i)
print(dem)

