x = "Chao mung den CLB Tin Hoc HIT"
print(x)

y = "CLB Tin Hoc HIT truc thuoc Khoa CNTT  - “10 diem”"
print(y)

a = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
lower =""
upper =""
for i in a:
    if i>="A" and i <="Z":
        lower = lower + i
    if i>="a" and i <= "z":
        upper = upper + i
print(lower)
print(upper)

if "CNTT" in a:
    print("Yes")
else:
    print("No")

a1 = ""
for i in a:
    if i>="A" and i <="Z":
        a1 = a1 + i.lower()
    if i>="a" and i <= "z":
        a1 = a1 + i.upper()
    if i == " ":
        a1 = a1 + " "
print(a1)