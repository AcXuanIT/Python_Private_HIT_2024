s = input("Nhap tu can dien :")

dem_s = {}
for i in s :
    if i not in dem_s.keys():
        dem_s[i] = 1
    else:
        dem_s[i] +=1

print(dem_s)