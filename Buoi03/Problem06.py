

def e(x):
    e = 1+x
    T = x
    M = 1
    for i in range(2,1000):
        T *= x
        M *= i
        e += T/M
    return e

def binary(x):
    if x < 0:
        return 0
    else:
        return 1

def sig(x):
    return 1/(1+e(-x))

def elu(x):
    if x >= 0:
        return x
    else:
        a = 0.01
        return a * (e(x) - 1 )
    
x = int(input("Nhap x : "))
h = input("Nhap ten ham kich hoạt : 1.binary 2.sigmoid 3.elu  :  ")

if(h == "binary"):
    print("Binary = ", binary(x))
if(h == "sigmoid"):
    print("Sigmoid = ", sig(x))
if(h == "elu"):
    print("Elu = ",elu(x))