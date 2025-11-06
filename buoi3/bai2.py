from os.path import split

from soupsieve.util import lower

chuoi=input("nhap 1 chuỗi bất kì: ")
chuoi.strip()
chuoi2=''.join([x for x in chuoi if x.isalpha() or x == ' '])
print("chuẩn hóa: ",lower(chuoi2).strip())
print("nguyên âm bao gồm: u,e,o,a,i")
nguyenAm=['u','e','o','a','i']
demNguyenAm=0
demPhuAm=0
for i in chuoi2:
    if i.lower() in nguyenAm and i.isalpha():
        demNguyenAm+=1
    elif i.isalpha() :
        demPhuAm+=1
print("nguyên âm: ",demNguyenAm,", phụ âm: ",demPhuAm)
chuoiDao=[]
listchuoi=list(map(str,chuoi2.split()))
for word in listchuoi:
    char=[i for i in word]
    char.reverse()
    char=''.join(char)
    chuoiDao.append(char)
print("dao tung tu: ",chuoiDao)

chuoichuan=''.join([x for x in chuoi if x.isalpha()]).strip()
if chuoichuan==chuoichuan[::-1]:
    print("true")
else:
    print("false")



