chuoi="TV, Laptop, Phone,TV, Tablet, Laptop, Camera"
list1=list(chuoi.split(","))
list1=set(list1)
list1=tuple(list1)

print("kho hang: ",list1)
print("so luong hang hoa: ", len(list1))
sanphambanchay={"Phone", "Laptop", "Smartwatch"}
banchay=[]
khongchay=[]
for i in list1:
    if i.strip() in sanphambanchay:
        banchay.append(i)
    else:
        khongchay.append(i)
print("san pham ban chay: ",banchay)
print("san pham kgong nam trong danh sach ban: ",khongchay)

