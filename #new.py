#교집합을 Return 하는 함수

def intersect(prelist,postlist):
    result=[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(intersect("HAM","SPAM"))

x=10
def func(a):
    return a+x

print(func(1))

def func2(a):
    x=5
    return a+x
print(func2(1))


def times(a=10,b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

def connectURI(Server,Port):
    strURL = "http://" + Server + ":" + Port
    return strURL

print(connectURI("multi.com","80"))