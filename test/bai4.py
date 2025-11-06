list1=list("1 2 3 4 8 9 10 11 12 6 ")
listSoNguyen=[x for x in list1 if x.isdigit()]
listSoNguyen=set(listSoNguyen)
listSoNguyen=list(listSoNguyen)
listSoNguyen.sort()
print(listSoNguyen)
a=[]
for i in range (len(listSoNguyen)-1):
    if int(listSoNguyen[i])+1==int(listSoNguyen[i+1]):
        a.append(listSoNguyen[i])
        a.append(listSoNguyen[i+1])
doanDaiNhat=set(a)
doanDaiNhat=list(doanDaiNhat)
doanDaiNhat.sort()
doantest=[]

for i in range (len(listSoNguyen)-1):
    if int(listSoNguyen[i])+1==int(listSoNguyen[i+1]):
        doantest.append(listSoNguyen[i])
        doantest.append(listSoNguyen[i+1])

doantest=set(doantest)
doantest=list(doantest)
doantest.sort()
doantest=tuple(doantest)
print(doantest)
c=len(doantest)


