def e(x):
    e = 1+x
    T = x
    M = 1
    for i in range(2,1000):
        T *= x
        M *= i
        e += T/M
    return e

def s(n):
    s = 1
    M = 1
    for i in range(2,n+1):
        M *= i
        s += 1/M
    return s

print(f"e^x = {e(5)}")
print(f"s(x) = {s(5)}")