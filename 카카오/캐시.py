from collections import deque

def solution(cacheSize,cities):
    deq = deque(maxlen=cacheSize)
    excute_time = 0
    for city in cities:
        city = city.lower()
        if city in deq:
            excute_time +=1
            deq.remove(city)
            deq.appendleft(city)
        else :
            excute_time +=5
            deq.appendleft(city)

    return excute_time
