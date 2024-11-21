dang_ky = {"An","Anh","Nam","Binh","Dong","Thu","Cuong","Khoa","Lam","Tuan","Hoa"}
check_in = {"An","Binh","Lam","Tuan","Hoa"}

chua_check_in = dang_ky - check_in
print("Danh sach chua check in :")
print(chua_check_in)

tong_so_luong = len(dang_ky) + len(check_in)
print("tong so luong :" , tong_so_luong)

dang_ky_sort = sorted(dang_ky)
print("ds dang ky sort : ", dang_ky_sort)