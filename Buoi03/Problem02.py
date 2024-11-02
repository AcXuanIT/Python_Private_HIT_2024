import math

n = int(input())

k = int(math.sqrt(n))
dem = 0
if k**2 != n:
    k += 1
for i in range(2,k):
    dem += 1
print(dem)
