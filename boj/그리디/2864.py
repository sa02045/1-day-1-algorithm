A,B = map(str,input().split())

def getMin(str):
    return int(str.replace("6","5"))
def getMax(str):
    return int(str.replace("5","6"))

print(getMin(A)+getMin(B), getMax(A)+getMax(B))

