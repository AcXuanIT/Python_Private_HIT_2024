"""
a = [1,2,3,4,5]
for x in a:
    print(x)

b = []
for i in range(1,201):
    if i%2==0:
        b.append(i);
print("len B :" , len(b))
print(b)

n = int(input())
c = []
sum = 0 
for i in range(n):
    c.append(int(input()))
    sum += c[i]
print(sum)
"""
#d =[]
n= 3
m= 3
"""
for i in range(n):
    d1 = []
    for j in range(n):
        d1.append(float(input()))
    d.append(d1)
"""
#for i in range(n):

#lst2 = [[int(input()) for i in range(n)] for j in range(m)]
"""
c = [1,2,3,4,5,6,7,8,9]
print(c.pop())
print(c)

b = c
e = c.copy()
c.append(10)
print(b)
print(e)
"""
"""
a = [1,6,3,8,3,6,4,7,9,8,2,5]
a.sort()
print(a)


print("Min a :", min(a))
print("Max a :", max(a))
index = -1
for i in range(len(a)):
    if a[i] % 2 == 0:
        index = i
        break;
if index != -1:
    print("Vi tri ptu chan dau tien :",index)

if 3 in a:
    print("Co ton tai 3")
else:
    print("Khong co");

k = 10
a.insert(k,2)
print(a)

for i in a[::-1] :
    if i % 2 == 0:
        a.remove(i)
print(a)
"""

#4
"""
a = [1,2,3,4,5,7]
m = int(input())
b = []
for i in range(m):
    p = int(input())
    b.append(p)

b = b + b
b.reverse
c = a + b
print(c)
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())

a = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):  
            a.append([i,j,k])
print(a)

for x in a:
    if x[0] + x[1] + x[2] == n:
        a.remove(x)

print(a)