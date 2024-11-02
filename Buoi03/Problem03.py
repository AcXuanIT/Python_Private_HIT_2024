
n = int(input())

def check(x):
    if x >= 190:
        return "Xuat sac"
    elif x >= 150:
        return "Gioi"
    elif x >= 100:
        return "Kha"
    else:
        return "Yeu"

for i in range(n):
    name = input()
    d1 = int(input())
    d2 = int(input())
    print(i, name , d1 + d2 , check(d1+d2))
