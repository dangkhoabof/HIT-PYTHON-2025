

chuoi="Xin CHao Moi moi nguoi"
chuoi=chuoi.strip()
chuoi=chuoi.lower()
chuoi2=list(map(str,chuoi.split()))
chuoi3=[]
for word in chuoi2:
    if word not in chuoi3:
        chuoi3.append(word)
print(chuoi3)
for word in chuoi3:
    print(f"\'{word}\' xuat hien { chuoi2.count(word)} lan")
maxChuoi=0
for i in range(len(chuoi3)):
    if len(chuoi3[i]) > len(chuoi3[maxChuoi]):
        maxChuoi = i
print("tu dai nhat la: ",chuoi3[maxChuoi])
xuatHienNhieuNhat=""
maxXuatHienNhieuNhat=0
for word in chuoi3:
    if chuoi2.count(word)>maxXuatHienNhieuNhat:
        xuatHienNhieuNhat=word
        maxXuatHienNhieuNhat=chuoi2.count(word)
print(xuatHienNhieuNhat)
tongkytu=0
for word in chuoi2:
    tongkytu+=len(word)
print(tongkytu)
for i in range(len(chuoi3)):
    for j in range(i+1,len(chuoi3)):
        if len(chuoi3[i]) < len(chuoi3[j]):
            tam=chuoi3[i]
            chuoi3[i]=chuoi3[j]
            chuoi3[j]=tam
print(chuoi3)



