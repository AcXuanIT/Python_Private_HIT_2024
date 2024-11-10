import random

k = int(input("Nhap k phan tu :"))
list = []

def nhapTuDong():
    for i in range(k):
        list.append(random.randint(1,20))
    print("Mang a la : ",list)

def nhapThuCong():
    for i in range(k):
        list.append(int(input()))

nhapTuDong()

n = int(input("Nhap n : "))
m = int(input("Nhap m : "))

def MaTran():
    maTran = []
    for i in range(0,m*n,m):
        h = []
        for j in range(i,i+m):
            h.append(list[j])
        maTran.append(h)

    print(maTran)

if n*m > k:
    print("Khong the xay dung duoc ma tran")
else:
    MaTran()