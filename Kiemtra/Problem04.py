data = [
    "name=Alice ; age=30; score=85.5 " ,
    "name=Bob ; age=25; score=90" ,
    "name=Alice ; age=30; score=92" ,
    "city=NewYork ; name=Eve ; age=35; score=88" ,
    "city=London ; name=Alice ; age=30; score=85.5"
]

data1 = {}

for x in data:
    x1 = x.split(";")
    lst = []
    for i in x1:
        x2 = i.split("=")
        if x2[0] not in data1.keys():
           data1[x2[0]] = x2[1]
        else:
           data1[x2[0]] += "|"+ x2[1]

for key,val in data1.items():
    s = str(val)
    k = s.split("|")
    data1[key] = k

print("dict = ")
for key,val in data1.items():
    print(key + ":"+str(val))


data2 = {}
for key,val in data1.items():
    lst = list(val)
    value = {}
    value["unique_count"] = len(lst)
    if val[0] is int:
        maxx = val[0]
        for i in val :
            if maxx < i :
                maxx = i
        value["max_values"]
    else:
        maxx = len(val[0])
        for i in val:
            if len(i) > maxx:
                maxx = len(i)
        value["max_length"] = maxx
    data2[f"{key}"] = value


print(data2)