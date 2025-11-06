

vanban="An:8.5, Binh:7.0, An:9.0, Cuong:6.5, Binh:8.0, Dung:7.5"
list1=vanban.split(',')
list2=[]
for i in list1:
    ten,diem=i.split(':')
    list2.append((ten.strip(),float(diem)))
print(list2)
tenduynhat=set()
for ten,dim in list2:
    tenduynhat.add(ten)
print(tenduynhat)
danhsachdiemTB=[]
for tendn in tenduynhat:
    tong=0
    dem=0
    for ten,diem in list2:
        if ten==tendn:
            tong+=diem
            dem+=1
    print(f"diem cua {tendn} la: {tong/dem}")
    danhsachdiemTB.append((tendn,tong/dem))




