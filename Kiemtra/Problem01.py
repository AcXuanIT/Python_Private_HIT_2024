n = 10001

def e(x):
    s = 1
    T = 1
    M = 1
    for i in range(1,n):
        T *= x
        M *= i
        s += T/M
    return s

x = int(input("Nhap x :"))
print(f"e({x}) = {e(x)}")
