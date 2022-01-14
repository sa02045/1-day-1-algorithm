
T=int(input())
times=[300,60,10]
times_cnt=[0,0,0]
for i in range(len(times)):
    cnt = 0
    while T >= times[i]:
        T -= times[i]
        cnt +=1
    times_cnt[i] = cnt

if T == 0:
    for cnt in times_cnt:
        print(cnt,end=" ")
else:
    print(-1)