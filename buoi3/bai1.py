numbers = [2, 3, 2, -4, 3, 5]
print(numbers)
numbers=set(numbers)
numbers=list(numbers)
print("sau khi loại trùng: ",numbers)
numbers_mu2=[]
trungBinhChan=0
for number in numbers:
    if number % 2 == 0:
        numbers_mu2.append(number**2)
    else:
        numbers_mu2.append(number**3)
print("list mới: ",numbers_mu2)
dem=0
for number in numbers:
    if dem%2==0:
        dem=dem+1
        trungBinhChan=trungBinhChan+number
    else:
        dem=dem+1
trungBinhChan=trungBinhChan/2
print("trung binh vị trí chẵn: ",trungBinhChan)
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if abs(numbers[i]>numbers[j]):
            tam = numbers[i]
            numbers[i]=numbers[j]
            numbers[j]=tam
print("sắp xếp theo abs: ",numbers)



