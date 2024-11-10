x=['a','b','c','d','r']
y=[1,2,3,4,5]



a = len(x)
b = len(y)
k = b if a > b else a
c = []

for i in range(k):
    c.append(x[i])
    c.append(y[i])

for i in range(k,a):
    c.append(x[i])

for i in range(k,b):
    c.append(y[i])

print(c)

