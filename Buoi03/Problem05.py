n = int(input())
name = []
foot = []
for i in range(n):
    namex = input()
    name.append(namex)

for i in range(n):
    footx = int(input())
    foot.append(footx)

sum_foot = 0
for i in range(n):
    if foot[i] >= 5:
        sum_foot += foot[i]
        if foot[i] > 100:
            break;

min_foot = 100000000
min_foot_index = -1
for i in range(n):
    if min_foot > foot[i]:
        min_foot = foot[i]
        min_foot_index = i

max_foot = -1
max_foot_index = -1
for i in range(n):
    if max_foot < foot[i]:
        max_foot = foot[i]
        max_foot_index = i

ds = list(zip(name,foot))
for i in range(n):
    print(ds[i])

print(sum_foot)
print(name[max_foot_index])
if min_foot < 5:
    print(min_foot)
else:
    print("Khong co")