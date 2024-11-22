coded_str = input("Nhap code_str : ")

coded = coded_str.split("[")

code = []
for i in coded:
    test = i.split("]")
    for x in test:
        code.append(x)

code2 = ""

for i in range(len(code)):
    k = code[i]
    if len(k) == 0 :
        continue
    if k[-1]>='1' and k[-1]<='9':
        code2 += k[0:len(k)-1]
        for j in range(int(k[-1])):
            code2 += code[i+1]
        i+=1

print("Output : " + code2)