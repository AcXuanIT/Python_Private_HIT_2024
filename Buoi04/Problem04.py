import random
import math

target = []
prediet = []

def Constructor(n):
    for i in range(n):
        target.append(random.uniform(0.0,10.0))
        prediet.append(random.uniform(0.0,10.0))

def MAE(n):
    s = 0
    for i in range(n):
        s += abs(target[i] - prediet[i])
    s = s/n
    return s

def MSE(n):
    s = 0
    for i in range(n):
        s += (target[i] - prediet[i])**2
    s = s/n    
    return s

def RMSE(n):
    return math.sqrt(MSE(n))

def Huber_Loss(n):
    o = 0.5
    s = 0
    for i in range(n):
        k = target[i] - prediet[i]
        if k <= o:
            s += 0.5*(k**2)
        else:
            s += o*abs(k)-0.5*o
    return s

n = int(input("Input number of samples : "))

if n < 0 : 
    print("number of samples must be a positive integer number")
else:
    Constructor(n)
    loss_name = input("Input loss name : ")
    print("Target : ",target)
    print("Prediet : ",prediet)

    if loss_name == "MAE":
        print(f"MAE: {MAE(n)}")
    elif loss_name == "MSE":
        print(f"MSE: {MSE(n)}")
    elif loss_name == "RMSE":
        print(f"RMSE: {RMSE(n)}")
    elif loss_name == "Huber_Loss":
        print(f"HUber_Loss: {Huber_Loss(n)}")
