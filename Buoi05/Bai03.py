input_dict = {}
n = int(input("Nhap so luong phan tu dict muon them :"))

for i in range(n):
    key = input("Nhap key : ")
    value = input("Nhap value : ")
    input_dict[key] = value

hoandoi_dict = {}
check = False

for key,value in input_dict.items():
    if value in hoandoi_dict:
        check = True
        break
    hoandoi_dict[value] = key

if check:
    print("None")
else:
    print("Dict hoan doi : ")
    print(hoandoi_dict)
