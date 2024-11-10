import random
#Nhap so luong phan tu 2 list
n = int(input("Nhap n :"))
m = int(input("Nhap m :"))

a = []
b = []

#Random phan tu trong 2 list
for i in range(n):
    a.append(random.randint(1,20))
for i in range(m):
    b.append(random.randint(1,15))

print(a)
print(b)

c=[]
for i in a:
    if i in b:
        c.append(i)
        b.remove(i)

print(c)