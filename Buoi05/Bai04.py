import random

n = int(input("Nhap n : "))

password = ["CNTT", "KHMT","KTPM", "HTTT", "DAPT"]

acc = {}

for i in range(n):
    msv = f"202360{str(i + 1).zfill(4)}"
    passw = random.choice(password) + msv
    acc[f"Account{i + 1}"] = {
        "Username": msv,
        "Password": passw
    }

for key,value in acc.items():
    print(key," : ")
    print("\t" , value)
