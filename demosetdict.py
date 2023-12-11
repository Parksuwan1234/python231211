#demosetdict.py
tp =(10,20,30)
print(len(tp))
def calc(a,b):
    return a+b,a*b

result = calc(3,4)
print(result)

print("id:%s,name:%s" % ("kim","김유신"))

a={1,2,3,4,5}
b={6,7,8,9,8}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

a=list((1,2,3))
a.append(4)
print(a)

device={'아이폰':5,'아이패드':10,'윈도우':20}
print(device)
print(device["아이폰"])
device["아이폰"]=6
print(device)
del device["아이폰"]
print(device)

phone={"kim":"111","lee":"222"}
print("kim in phone")
p=phone
print(phone)
print(p)
print(id(phone),id(p))
del p["kim"]
print(phone)