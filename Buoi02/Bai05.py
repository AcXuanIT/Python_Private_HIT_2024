a = int(input())

s = ""

while a > 0 :
    s = str( a%8 ) + s
    a //= 8

x = len(s)*3
if s[0] == "1":
    x = x-2
if s[0] == "2" or s[0] == "3":
    x = x-1
print(f"So bíts can la : {x}")

b = int(input())
x = dir(b)
for i in x:
    print(i)



