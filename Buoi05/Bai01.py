#Nhập vào từ bàn phím 2 tuple A và B
At = tuple(input("Nhap A :").split())
A = tuple(int(x) for x in At)
B = tuple(input("Nhap B :").split())

#số lượng phần tử trong A mà có giá trị lớn hơn trung bình cộng của tất cả phần tử
avg = sum(A)/len(A)
avg_tuple = tuple(i for i in A if i > avg)
print(avg_tuple)

#Chia tuple A thành hai tuple con
A_chan = tuple(i for i in A if i % 2 == 0)
A_le = tuple(i for i in A if i % 2 != 0)
print(A_chan)
print(A_le)

#Nhập vào bàn phím ký tự k, đếm số lần xuất hiện của k trong B
k = input("Nhap k : ")
dem = 0
for x in B:
    if k in x:
        dem+=1
print("So lan xuat hien cua k :" , dem)

#Tìm các phần tử trong tuple B có độ dài lớn hơn hoặc bằng 5 ký tự.
B5 = tuple(i for i in B if len(i) >= 5)
print(B5)

#Ghep
C = tuple(zip(A,B))
print(C)